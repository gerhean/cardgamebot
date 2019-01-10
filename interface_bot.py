import json
import requests
import time
import urllib
from uno_rules import game_manager
from bot_token import TOKEN


URL = "https://api.telegram.org/bot{}/".format(TOKEN)
ID_COMMAND = "/uno"


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


to_delete = []


def handle_updates(updates):
    global to_delete
    for update in updates["result"]:
        print(update)
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            player_name = update["message"]["from"]["username"]
            message_id = update["message"]["message_id"]
        except KeyError:
            print(KeyError)
            continue
        if text.startswith(ID_COMMAND):
            if to_delete:
                for del_message_id in to_delete:
                    delete_message(chat, del_message_id)
                to_delete = []
            command = text.split(" ")
            message = game_manager(player_name, command[1:])
            reply_to = None
            if message["items"]:
                reply_markup = build_keyboard(message["items"])
                if message["is_reply"]:
                    reply_to = message_id
            else:
                reply_markup = None
            print(message["text"])
            sent = send_message(message["text"], chat, reply_markup, reply_to)
            if message["del_post"]:
                to_delete.append(message_id)
            if message["instant_del"]:
                try:
                    to_delete.append(json.loads(sent)["result"]["message_id"])
                except:
                    print("post not found")
        else:
            continue


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def build_keyboard(items):
    keyboard = [[ID_COMMAND + " " + item] for item in items]
    reply_markup = {"keyboard":keyboard, "one_time_keyboard": True, "selective": True}
    return json.dumps(reply_markup)


def send_message(text, chat_id, reply_markup=None, reply_to=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup is not None:
        url += "&reply_markup={}".format(reply_markup)
    if reply_to is not None:
        url += "&reply_to_message_id={}".format(reply_to)
    return get_url(url)


def delete_message(chat_id, message_id):
    url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
    get_url(url)


def main():
    print("starting")
    updates = get_updates(None)
    last_update_id = updates["result"][-1]["message"]["message_id"]
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.1)


if __name__ == '__main__':
    main()