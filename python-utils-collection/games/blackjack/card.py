from constants import CARD_VALUE_MAP

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value =CARD_VALUE_MAP[rank.upper()]

    def __str__(self):
        return self.rank + '('+str(self.value) + ') of ' + self.suit
