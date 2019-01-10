from random import shuffle, randint


class Pile:
    def __init__(self):
        self.cards = []

    def draw(self):
        return self.cards.pop()

    def shuffle(self):
        shuffle(self.cards)

    def take_rand(self):
        return self.cards.pop(randint(0, len(self.cards)))

    def place(self, card, pos=None):
        if pos is None:
            self.cards.append(card)
        else:
            self.cards.insert(pos, card)


