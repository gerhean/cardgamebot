from random import shuffle, randint
from unocardlist import uno_card_list


class Pile:
    def __init__(self, card_list, cards=None):
        if cards is not None:
            self.cards = cards
        else:
            self.cards = []
        self.card_list = card_list

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def take_rand(self):
        return self.cards.pop(randint(0, len(self.cards)))

    def take(self, pos):
        return self.cards.pop(pos)

    def place(self, card, pos=None):
        if pos is None:
            self.cards.append(card)
        else:
            self.cards.insert(pos, card)

    def peek_top(self, num=1):
        return self.cards[-1 * num:]

    def get_pos(self, name):
        try:
            return self.cards.index(name)
        except ValueError:
            return None

    def __len__(self):
        return len(self.cards)

    def get_card_with_props(self, properties):
        for pos, card in enumerate(self.cards):
            found = True
            for key in properties:
                if properties.key != self.card_list[card].key:
                    found = False
            if found:
                return pos
        return None

    def empty_pile(self):
        old_cards = self.cards
        self.cards=[]
        return old_cards

    def add_pile_to_top(self, new_cards: list):
        self.cards += new_cards


class UnoGameRoom:
    def fill_deck(self, card_list):
        deck = []
        for card in card_list:
            for i in range(card_list[card]["copies"]):
                deck.append(card)
        return deck

    def __init__(self, room_id, player_num, card_list):
        self._card_list = card_list
        self.room_id = room_id
        self.deck = Pile(card_list, self.fill_deck(card_list))
        self.deck.shuffle()
        self.discard = Pile(card_list)
        self._player_hands = []
        self._player_num = player_num
        self._players = []
        self.direction = 1
        self.game_state = ""
        self.turn = 0
        self.wild_color = "Red"
        for i in range(player_num):
            hand = Pile(card_list)
            for j in range(7):
                hand.place(self.deck.draw())
            self._player_hands.append(hand)
        self.discard.place(self.deck.draw())
        while self.discard.peek_top()[0] == "Wild":
            self.discard.place(self.deck.draw())

    def add_player(self, player):
        if not self.full_room():
            self._players.append(player)
            return True
        else:
            return False

    def full_room(self):
        return len(self._players) == self._player_num

    def get_hand(self, turn):
        return self._player_hands[turn]

    def get_hand_by_player(self, player):
        try:
            return self.get_hand(self._players.index(player))
        except ValueError:
            return None

    def next_turn(self):
        self.turn += self.direction
        if self.turn >= self._player_num:
            self.turn -= self._player_num
        elif self.turn < 0:
            self.turn = self._player_num + self.turn

    def current_player(self):
        return self._players[self.turn]

    def current_player_actions(self):
        return ["draw"] + list(map(lambda x: "place " + x, self.get_hand(self.turn).cards))

    def all_player_info(self, hand_size=False):
        players = []
        for turn, player in enumerate(self._players):
            info = {"name":player, "turn":turn}
            if hand_size:
                info["hand_size"] = len(self.get_hand_by_player(player))
            players.append(info)
        return players

    def refresh_deck(self):
        if len(self.deck) <= 2:
            top = self.discard.draw()
            cards = self.discard.empty_pile()
            self.discard.place(top)
            self.deck.add_pile_to_top(cards)
            self.deck.shuffle()

    def __contains__(self, player):
        try:
            self._players.index(player)
            return True
        except ValueError:
            return False


def make_message(message: str,
                 items: list = [],
                 is_reply: bool = False,
                 del_post: bool = False,
                 instant_del: bool = False) -> dict:
    return {"text": message,
            "items": items,
            "is_reply": is_reply,
            "del_post": del_post,
            "instant_del": instant_del}


colors = ["Red", "Blue", "Green", "Yellow"]
rooms = {}


def game_manager(player, text, chat_id):
    global colors
    if chat_id not in rooms:
        rooms[chat_id] = None
    room = rooms(chat_id)

    if len(text) == 0:
        return make_message("List of commands",
                            ["start int",
                             "end",
                             "join",
                             "see hand",
                             "see info",
                             "draw"],
                            is_reply=True,
                            del_post=True,
                            instant_del=True
                            )

    if room is None:
        if text[0] == "start":
            if len(text) == 2:
                try:
                    int(text[1])
                except ValueError:
                    return make_message("Only can start with 1-7 whole ppl", del_post=True, instant_del=True)
                if 0 < int(text[1]) < 8:
                    rooms[chat_id] = UnoGameRoom(1, int(text[1]), uno_card_list)
                    return make_message("Game started")
                else:
                    return make_message("Only can start with 1-7 whole ppl", del_post=True, instant_del=True)
        return make_message("Please 'start <number of players>' the game first", instant_del=True)

    elif text[0] == "end" and player in room:
        rooms[chat_id] = None
        return make_message("Game ended", del_post=True)

    elif not room.full_room():
        if text[0] == "join" and not player in room:
            room.add_player(player)
            return_text = player + " joined game"
            if room.full_room():
                return_text += "\nGame will now start!"
                return_text += "\nTop card is " + room.discard.peek_top()[0]
                return_text += "\nIt's @" + room.current_player() + " 's turn!"
                return make_message(return_text, room.current_player_actions())
            return make_message(return_text)
        else:
            return make_message("Need more ppl to start game", instant_del=True)

    else:
        if not player in room:
            return make_message("Please be a good spectator", instant_del=True)
        turn = room.turn

        if room.game_state == "wild":
            if text[0] in colors and player == room.wild_color:
                room.wild_color = text[0]
                room.game_state = "normal"
                return make_message("Card Wild " + text[0] + " placed!\nIt's " + room.current_player() + "'s turn now!",
                                    room.current_player_actions(), del_post=True)
            else:
                return make_message("Choose color?", colors, del_post=True, instant_del=True)

        if text[0] == "see":
            if text[1] == "hand":
                hand = room.get_hand_by_player(player)
                if player == room.current_player():
                    return make_message(player + " looked at own hand",
                                        room.current_player_actions(), is_reply=True,
                                        del_post=True, instant_del=True)
                else:
                    return make_message(player + " looked at own hand", hand.cards, True,
                                        del_post=True, instant_del=True)
            if text[1] == "info":
                return_text = ""
                infos = room.all_player_info(True)
                for info in infos:
                    return_text += str(info["name"]) + ": turn order: " + str(info["turn"])
                    return_text += ", hand size: " + str(info["hand_size"]) + "\n"
                return_text += "turn direction: " + str(room.direction)
                return_text += "\ntop card: " + room.discard.peek_top()[0]
                return make_message(return_text)

        if player == room.current_player():
            if text[0] == "draw":
                hand = room.get_hand(turn)
                hand.place(room.deck.draw())
                room.refresh_deck()
                return make_message(player + " drew a card", room.current_player_actions(),
                                    is_reply=True, del_post=True, instant_del=True)

            elif text[0] == "place":
                if len(text) < 2 or len(text) > 3:
                    return make_message("Invalid card", room.current_player_actions(), is_reply=True,
                                        del_post=True, instant_del=True)
                card_name = " ".join(text[1:])
                hand = room.get_hand(turn)
                card = hand.get_pos(card_name)
                if card is not None:
                    top = room.discard.peek_top()[0]
                    top_card = uno_card_list[top]
                    placed_card = uno_card_list[card_name]
                    card_type = placed_card["type"]
                    if top == "Wild":
                        placed_color = room.wild_color
                    else:
                        placed_color = placed_card["color"]
                    if top_card["color"] == placed_color or top_card["num"] == placed_card["num"] or card_type == "wild":
                        room.discard.place(hand.take(card))
                        if len(hand) == 0:
                            rooms[chat_id] = None
                            return make_message("Game ended, " + player + " won!")
                        else:
                            room.next_turn()
                            if card_type == "skip":
                                room.next_turn()
                            elif card_type == "reverse":
                                room.direction = -1
                                room.next_turn()
                                room.next_turn()
                            elif card_type == "+2":
                                turn = room.turn
                                hand = room.get_hand(turn)
                                hand.place(room.deck.draw())
                                hand.place(room.deck.draw())
                            elif card_type == "wild":
                                room.game_state = "wild"
                                room.wild_color = player
                                return make_message("Choose color?", colors, True)
                            return make_message("Card " + card_name + " placed!\nIt's @"
                                                + room.current_player() + " 's turn now!",
                                                room.current_player_actions(), del_post=True)
                return make_message("Invalid card", room.current_player_actions(),
                                    True, del_post=True, instant_del=True)

    return make_message("Invalid Command")


# game_manager("1", "start 2")
# while True:
#     player = input("player")
#     text = input("text")
#     game_manager(player, text)
