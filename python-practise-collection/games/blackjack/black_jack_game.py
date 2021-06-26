from card import Card
from deck import Deck
from player import Player


def display_current_info(player, computer, game_on):
    player_cards_content = ' ,'.join(str(p) for p in player.cards)
    print(f'{player.name}\' card is:' + player_cards_content)
    if not game_on:
        print(f'{player.name}\' total amount of money:' + str(player.amount))
    if game_on:
        computer_cards_content = ' ,'.join(str(p) for p in computer.cards[1:])
        print('Computer\' card is: Hidden, ' + computer_cards_content)
    else:
        computer_cards_content = ' ,'.join(str(p) for p in computer.cards)
        print('Computer\' card is: ' + computer_cards_content)
    if not game_on:
        print(f'Computer\' total amount of money:' + str(computer.amount))


def player_input_action():
    user_input = None
    while user_input not in ['HIT', 'STAND']:
        user_input = input("Do you want to HIT or STAND?")
    return user_input


def get_bet_amount(player):
    user_input = 0
    while int(user_input) <= 0 or int(user_input) > player.amount:
        user_input = input(
            f'How many do you want to bet? you have {player.amount}:')
    return int(user_input)


def player_continue():
    user_input = None
    while user_input not in ['Y', 'N']:
        user_input = input("Do you want to continue or not? answer Y or N: ")
    return True if user_input == 'Y' else False


def make_move(decision):
    if decision == 'HIT':
        player.add_card(deck.get_one())
    else:
        computer.add_card(deck.get_one())


def check_win(player, computer):
    if player.amount <= 0:
        print('Computer win, player broken!')
        return True
    elif computer.amount <= 0:
        print('Player win, Computer broken')
        return True
    return False


def check_current_turn_win(player, computer, player_decision, bet_amount):
    player_score = sum(card.value for card in player.cards)
    computer_score = sum(card.value for card in computer.cards)
    if player_decision == 'HIT':
        if player_score > 21:
            print(
                f'Computer Win! Computer Score: {str(computer_score)}, Player Score: {str(player_score)}')
            player.amount = player.amount-bet_amount
            return True
    else:
        if computer_score > 21:
            print(
                f'{player.name} Win! Computer Score: {str(computer_score)}, Player Score: {str(player_score)}')
            computer.amount = computer.amount-bet_amount
            return True
        elif computer_score > player_score:
            print(
                f'Computer Win! Computer Score: {str(computer_score)}, Player Score: {str(player_score)}')
            player.amount = player.amount-bet_amount
            return True
    return False
# -----------------game on ----------------


print('Welcome to Black Jack Game!')
player = Player(input('Please input your name: '), 100)
computer = Player('Computer', 100)

game_on = True
while game_on:
    # set up game
    bet_amount = get_bet_amount(player)
    deck = Deck()
    deck.shuffle()
    player.cards = []
    computer.cards = []
    for i in range(2):
        player.add_card(deck.get_one())
        computer.add_card(deck.get_one())
    turn_continue = True

    display_current_info(player, computer, turn_continue)
    player_decision = player_input_action()
    while turn_continue and player_decision == 'HIT':
        player.add_card(deck.get_one())
        turn_continue = not check_current_turn_win(
            player, computer, player_decision, bet_amount)
        display_current_info(player, computer, turn_continue)
        if turn_continue:
            player_decision = player_input_action()
    while turn_continue and player_decision == 'STAND':
        computer.add_card(deck.get_one())
        turn_continue = not check_current_turn_win(
            player, computer, player_decision, bet_amount)
        display_current_info(player, computer, turn_continue)

    game_on = (not check_win(player, computer)) and player_continue()


# add amount of money count
# add ace rule

# total money, picking betting amount
# track of total money
# when all money is gone , then lost
