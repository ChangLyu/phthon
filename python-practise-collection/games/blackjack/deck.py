from constants import CARD_SUIT, CARD_RANK
from card import Card
import random
class Deck:
    def __init__(self):
        self.cards=[]
        for suit in CARD_SUIT:
            for rank in CARD_RANK:
                self.cards.append(Card(suit,rank))
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def get_one(self):
        # default get the last one
        return self.cards.pop()