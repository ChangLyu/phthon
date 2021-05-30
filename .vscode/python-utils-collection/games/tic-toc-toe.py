from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' '+ board[7]+ ' | '+ board[8]+' | '+board[9]+' ')
    print('---|---|---')
    print(' '+board[4]+ ' | '+ board[5]+ ' | '+board[6]+' ')
    print('---|---|---')
    print(' '+board[1]+ ' | '+ board[2]+ ' | '+board[3]+' ')


def player_input():
    user_input = 'Wrong'
    while user_input not in ['X','O']:
        clear_output()
        user_input = input("Please pick a marker 'X' or 'O' : ")
    player1 = user_input
    player2 = 'X' if player1=='O' else 'O'
    print('player1 is: '+player1, 'player2 is: '+player2)
    return (player1,player2)

def place_marker(board, marker, position):
    board[position]=marker
  
def win_check(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or # across bottom
    (board[4] == board[5] == board[6] == marker) or # across middle
    (board[7] == board[8] == board[9] == marker) or # across top
    (board[1] == board[4] == board[7] == marker) or # down left
    (board[2] == board[5] == board[8] == marker) or # down middle
    (board[3] == board[6] == board[9] == marker) or # down right
    (board[1] == board[5] == board[9] == marker) or # diagonal
    (board[3] == board[5] == board[7] == marker))  # diagonal
    
import random
def choose_first():
    result= random.randint(1,3) 
    if result == 1:
        print('Player1 go first')
        
        return 'Player1'
    else:
        print('Player2 go first')
        return 'Player2'
    
def space_check(board, position):
    return False if (board[position]== 'X' or board[position]=='O') else True

def full_board_check(board):
    for i in board[1:]:
        if i not in ['X','O']:
            return False
    return True

def player_choice(board,player, marker):
    is_free= False
    while not is_free: 
        position = int(input('It is ' + player+ '\' turn, your maker is ' +marker+' Please select a position(1-9) you want to place : ')) 
        if position not in [1,2,3,4,5,6,7,8,9]:
            print("Your input not in range(1-9)")
        else:
            is_free=space_check(board,position)
            if not is_free:
                print('The position you select is occupied, please select a new one')
            else:
                return position

def replay():
    play_again='Wrong'
    while play_again not in ['Y','N']:
        play_again = input("Do you want to play again: 'Y' or 'N' : ")
        if play_again not in ['Y','N']:
            print("Please input 'Y' or 'N'")
        
    return play_again == 'Y'




print('Welcome to Tic Tac Toe!')
play_again = True
while play_again:
    board = [' ']*10
    (player1_maker,player2_maker)=player_input()
    turn = choose_first()
    game_on = True
    while game_on:

        display_board(board)
        
        if turn == 'Player1': 
            player1_position = player_choice(board, 'Player1', player1_maker)
            place_marker(board,player1_maker,player1_position)

            if win_check(board, player1_maker):
                display_board(board)
                print('Congras! Player1 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board()
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player2'
        else:
            player2_position = player_choice(board, 'Player2', player2_maker)
            place_marker(board,player2_maker,player2_position)
            if win_check(board, player2_maker):
                display_board(board)
                print('Congras! Player2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board()
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player1'
    
    play_again=replay()

    