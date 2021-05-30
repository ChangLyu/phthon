from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(' '+ board[7]+ ' | '+ board[8]+' | '+board[9]+' ')
    print('---|---|---')
    print(' '+board[4]+ ' | '+ board[5]+ ' | '+board[6]+' ')
    print('---|---|---')
    print(' '+board[1]+ ' | '+ board[2]+ ' | '+board[3]+' ')


def player_input():
    user_input = None
    while user_input not in ['X','O']:
        clear_output()
        user_input = input("Please pick a marker 'X' or 'O' : ")
    player1 = user_input
    player2 = 'X' if player1=='O' else 'O'
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

def choose_first_ML():
    result= random.randint(1,3) 
    if result == 1:
        print('Player go first')
        
        return 'Player'
    else:
        print('Machine go first')
        return 'Machine'
       
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
            
def copy_board(board):
    copy_board = []
    for i in board:
        copy_board.append(i)
    return copy_board

def randomChoiceFromMoveList(board, list):
    empty_list=[]
    for i in list:
        if space_check(board, i):
           empty_list.append(i) 
    if len(empty_list)!=0:
        return random.choice(empty_list)
    else: 
        return None

def machine_choice(board, machine_marker, player_marker):
    # first check if machine can win in next move
    for position in range(1,10):
        if space_check(board, position):
            copyed_board = copy_board(board)
            place_marker(copyed_board, machine_marker, position)
            if win_check(copyed_board, machine_marker):
                return position
    
    # second check is user will win in next move, if yes, block it 
    for position in range(1,10):
        if space_check(board, position):
            copyed_board = copy_board(board)
            place_marker(copyed_board, player_marker, position)
            if win_check(copyed_board, player_marker):
                return position
    
    # take corner if empty
    move= randomChoiceFromMoveList(board, [1,3,7,9])
    if move != None:
        return move
    # take center if empty
    if space_check(board, 5):
        return 5
        
    # take sides if empty
    return randomChoiceFromMoveList(board, [2,4,6,8])
 




def replay():
    play_again='Wrong'
    while play_again not in ['Y','N']:
        play_again = input("Do you want to play again: 'Y' or 'N' : ")
        if play_again not in ['Y','N']:
            print("Please input 'Y' or 'N'")
        
    return play_again == 'Y'
