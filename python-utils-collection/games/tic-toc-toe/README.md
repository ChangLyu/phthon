 7 | 8 | 9  
---|---|---
 4 | 5 | 6  
---|---|---
 1 | 2 | 3  

## TIC TOC TOE GAME WITH PLAYERS
1. play game
    1. Initial board
    2. player select marker X or O
    3. randomly choose which player go first
    4. game on
        1. display board
        2. player first go play
            1. choose position to place marker on board
            2. place marker
            3. check win or tie or continue
                1. if win: show board and win message and end this game
                2. if tie: show board and tie message and end this game
                3. continue play
        3. player second go play
            1. choose position to place marker on board
            2. place marker
            3. check win or tie or continue
                1. if win: show board and win message and end this game
                2. if tie: show board and tie message and end this game
                3. continue play
2. ask user want play again or end game


## TIC TOC TOE GAME WITH MACHINE
machine algorithm:
·        First, see if there’s a move the computer can make that will win the game. If there is, take that move. Otherwise, go to the second step.

·        Second, see if there’s a move the player can make that will cause the computer to lose the game. If there is, the computer should move there to block the player. Otherwise, go to the third step.

·        Third, check if the center is free. If so, move there. If it isn’t, then go to the fifth step.

·        Fourth, check if any of the corner spaces (spaces 1, 3, 7, or 9) are free. If no corner space is free, then go to the fourth step.


·        Fifth, move on any of the side pieces (spaces 2, 4, 6, or 8). There are no more steps, because if the execution has reached this step then the side spaces are the only spaces left.