
class Player:
    def __init__(self, name):
        self.cards = []
        self.name = name

    def add_card(self, cards):
        if isinstance(cards, list):
            self.cards.extend(cards)
        else:
            self.cards.append(cards)

    def get_one(self):
        return self.cards.pop(0)

    def __str__(self):
        return f'Play {self.name} has {len(self.cards)} cards.'
    
