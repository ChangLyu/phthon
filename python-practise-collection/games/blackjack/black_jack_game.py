from card import Card
from deck import Deck
from player import Player


print('Welcome to Black Jack Game!')
# set up game
deck = Deck()
deck.shuffle()

player = Player(input('Please input your name: '), 100)
computer = Player('Computer', 100)


for i in range(2):
    player.add_card(deck.get_one())
    computer.add_card(deck.get_one())


def display_cards(player, computer, game_on):
    player_cards_content = ' ,'.join(str(p) for p in player.cards)
    print(f'{player.name}\' card is:' + player_cards_content)
    if game_on:
        computer_cards_content = ' ,'.join(str(p) for p in computer.cards[1:])
        print('Computer\' card is: Hidden, ' + computer_cards_content)
    else:
        computer_cards_content = ' ,'.join(str(p) for p in computer.cards)
        print('Computer\' card is: ' + computer_cards_content)


def player_input_action():
    user_input = None
    while user_input not in ['HIT', 'STAND']:
        user_input = input("Do you want to HIT or STAND?")
    return user_input


def make_move(decision):
    if decision == 'HIT':
        player.add_card(deck.get_one())
    else:
        computer.add_card(deck.get_one())


def check_win(player, computer, player_decision):
    player_score = sum(card.value for card in player.cards)
    computer_score = sum(card.value for card in computer.cards)
    if player_decision == 'HIT':
        if player_score > 21:
            print(
                f'Computer Win! Computer Score: {computer_score}, Player Score: {player_score}')
            return True
    else:
        if computer_score > 21:
            print(
                f'{player.name} Win! Computer Score: {computer_score}, Player Score: {player_score}')
            return True
        elif computer_score > player_score:
            print(
                'Computer Win! Computer Score: {computer_score}, Player Score: {player_score}')
            return True
    return False
# -----------------game on ----------------


game_on = True
while game_on:

    display_cards(player, computer, game_on)
    if game_on:

        player_decision = player_input_action()
        while game_on and player_decision == 'HIT':
            player.add_card(deck.get_one())
            game_on = not check_win(player, computer, player_decision)
            display_cards(player, computer, game_on)
            if game_on:
                player_decision = player_input_action()

        while game_on and player_decision == 'STAND':
            computer.add_card(deck.get_one())
            game_on = not check_win(player, computer, player_decision)
            display_cards(player, computer, game_on)


# add amount of money count
# add ace rule

# total money, picking betting amount
# track of total money
# when all money is gone , then lost
