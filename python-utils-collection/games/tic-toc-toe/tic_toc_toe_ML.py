from tic_toc_toe_utils import * 




print('Welcome to Tic Tac Toe, play with Machine!')
play_again = True
while play_again:
    board = [' ']*10
    (player_marker,machine_maker)=player_input()
    print('player is: '+player_marker, 'Machine is: '+machine_maker)
    turn = choose_first_ML()
    
    game_on = True
    while game_on:

        display_board(board)
        
        if turn == 'Player': # player's turn
            player_position = player_choice(board, 'Player', player_marker)
            place_marker(board,player_marker,player_position)

            if win_check(board, player_marker):
                display_board(board)
                print('Congras! Player has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Machine'
        else: # machine's turn
            machine_position = machine_choice(board, machine_maker,player_marker)
            print('Machine has placed in: '+ str(machine_position))
            place_marker(board,machine_maker,machine_position)
            if win_check(board, machine_maker):
                display_board(board)
                print('Congras! Machine has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player'
    
    play_again=replay()

    