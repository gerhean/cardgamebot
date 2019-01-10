def create_card_list():
    def create_card(color, num, card_type, copies):
        card = {"color": color, "num": num, "type": card_type, "copies": copies}
        if card_type == "none":
            name = color + " " + str(num)
        elif card_type == "wild":
            name = "Wild"
        else:
            name = color + " " + card_type
        cards[name] = card

    cards = {}
    for color in ["Red", "Blue", "Green", "Yellow"]:
        for i in range(9):
            create_card(color, i + 1, "none", 2)
        create_card(color, 10, "skip", 2)
        create_card(color, 11, "reverse", 2)
        create_card(color, 12, "+2", 2)
    create_card("multi", 0, "wild", 4)
    return cards


uno_card_list = {
  'Red 1': {
    'color': 'Red',
    'num': 1,
    'type': 'none',
    'copies': 2
  },
  'Red 2': {
    'color': 'Red',
    'num': 2,
    'type': 'none',
    'copies': 2
  },
  'Red 3': {
    'color': 'Red',
    'num': 3,
    'type': 'none',
    'copies': 2
  },
  'Red 4': {
    'color': 'Red',
    'num': 4,
    'type': 'none',
    'copies': 2
  },
  'Red 5': {
    'color': 'Red',
    'num': 5,
    'type': 'none',
    'copies': 2
  },
  'Red 6': {
    'color': 'Red',
    'num': 6,
    'type': 'none',
    'copies': 2
  },
  'Red 7': {
    'color': 'Red',
    'num': 7,
    'type': 'none',
    'copies': 2
  },
  'Red 8': {
    'color': 'Red',
    'num': 8,
    'type': 'none',
    'copies': 2
  },
  'Red 9': {
    'color': 'Red',
    'num': 9,
    'type': 'none',
    'copies': 2
  },
  'Red skip': {
    'color': 'Red',
    'num': 10,
    'type': 'skip',
    'copies': 2
  },
  'Red reverse': {
    'color': 'Red',
    'num': 11,
    'type': 'reverse',
    'copies': 2
  },
  'Red +2': {
    'color': 'Red',
    'num': 12,
    'type': '+2',
    'copies': 2
  },
  'Blue 1': {
    'color': 'Blue',
    'num': 1,
    'type': 'none',
    'copies': 2
  },
  'Blue 2': {
    'color': 'Blue',
    'num': 2,
    'type': 'none',
    'copies': 2
  },
  'Blue 3': {
    'color': 'Blue',
    'num': 3,
    'type': 'none',
    'copies': 2
  },
  'Blue 4': {
    'color': 'Blue',
    'num': 4,
    'type': 'none',
    'copies': 2
  },
  'Blue 5': {
    'color': 'Blue',
    'num': 5,
    'type': 'none',
    'copies': 2
  },
  'Blue 6': {
    'color': 'Blue',
    'num': 6,
    'type': 'none',
    'copies': 2
  },
  'Blue 7': {
    'color': 'Blue',
    'num': 7,
    'type': 'none',
    'copies': 2
  },
  'Blue 8': {
    'color': 'Blue',
    'num': 8,
    'type': 'none',
    'copies': 2
  },
  'Blue 9': {
    'color': 'Blue',
    'num': 9,
    'type': 'none',
    'copies': 2
  },
  'Blue skip': {
    'color': 'Blue',
    'num': 10,
    'type': 'skip',
    'copies': 2
  },
  'Blue reverse': {
    'color': 'Blue',
    'num': 11,
    'type': 'reverse',
    'copies': 2
  },
  'Blue +2': {
    'color': 'Blue',
    'num': 12,
    'type': '+2',
    'copies': 2
  },
  'Green 1': {
    'color': 'Green',
    'num': 1,
    'type': 'none',
    'copies': 2
  },
  'Green 2': {
    'color': 'Green',
    'num': 2,
    'type': 'none',
    'copies': 2
  },
  'Green 3': {
    'color': 'Green',
    'num': 3,
    'type': 'none',
    'copies': 2
  },
  'Green 4': {
    'color': 'Green',
    'num': 4,
    'type': 'none',
    'copies': 2
  },
  'Green 5': {
    'color': 'Green',
    'num': 5,
    'type': 'none',
    'copies': 2
  },
  'Green 6': {
    'color': 'Green',
    'num': 6,
    'type': 'none',
    'copies': 2
  },
  'Green 7': {
    'color': 'Green',
    'num': 7,
    'type': 'none',
    'copies': 2
  },
  'Green 8': {
    'color': 'Green',
    'num': 8,
    'type': 'none',
    'copies': 2
  },
  'Green 9': {
    'color': 'Green',
    'num': 9,
    'type': 'none',
    'copies': 2
  },
  'Green skip': {
    'color': 'Green',
    'num': 10,
    'type': 'skip',
    'copies': 2
  },
  'Green reverse': {
    'color': 'Green',
    'num': 11,
    'type': 'reverse',
    'copies': 2
  },
  'Green +2': {
    'color': 'Green',
    'num': 12,
    'type': '+2',
    'copies': 2
  },
  'Yellow 1': {
    'color': 'Yellow',
    'num': 1,
    'type': 'none',
    'copies': 2
  },
  'Yellow 2': {
    'color': 'Yellow',
    'num': 2,
    'type': 'none',
    'copies': 2
  },
  'Yellow 3': {
    'color': 'Yellow',
    'num': 3,
    'type': 'none',
    'copies': 2
  },
  'Yellow 4': {
    'color': 'Yellow',
    'num': 4,
    'type': 'none',
    'copies': 2
  },
  'Yellow 5': {
    'color': 'Yellow',
    'num': 5,
    'type': 'none',
    'copies': 2
  },
  'Yellow 6': {
    'color': 'Yellow',
    'num': 6,
    'type': 'none',
    'copies': 2
  },
  'Yellow 7': {
    'color': 'Yellow',
    'num': 7,
    'type': 'none',
    'copies': 2
  },
  'Yellow 8': {
    'color': 'Yellow',
    'num': 8,
    'type': 'none',
    'copies': 2
  },
  'Yellow 9': {
    'color': 'Yellow',
    'num': 9,
    'type': 'none',
    'copies': 2
  },
  'Yellow skip': {
    'color': 'Yellow',
    'num': 10,
    'type': 'skip',
    'copies': 2
  },
  'Yellow reverse': {
    'color': 'Yellow',
    'num': 11,
    'type': 'reverse',
    'copies': 2
  },
  'Yellow +2': {
    'color': 'Yellow',
    'num': 12,
    'type': '+2',
    'copies': 2
  },
  'Wild': {
    'color': 'multi',
    'num': 0,
    'type': 'wild',
    'copies': 4
  }
}