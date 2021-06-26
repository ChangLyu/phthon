from tic_toc_toe_utils import * 



print('Welcome to Tic Tac Toe!')
play_again = True
while play_again:
    board = [' ']*10
    (player1_maker,player2_maker)=player_input()
    print('player1 is: '+player1_maker, 'player2 is: '+player2_maker)
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
                    display_board(board)
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
                    display_board(board)
                    print("TIE GAME")
                    game_on = False
                else:
                    turn = 'Player1'
    
    play_again=replay()

    