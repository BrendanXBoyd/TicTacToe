"""Player 1 is 1, player 2 is 2.  Each turn, the player inputs which square they want
The square is filled with a 1 or 2 (unless already full)
When there is a completed win, or a full board, the game ends"""

################ Imports ################
import numpy as np

################ CLASSES ################
class GameBoard:
    #Create initialization funtion
    def __init__(gb, boardSize = 3):
        gb.N = boardSize
        gb.B = np.zeros((boardSize,boardSize))

    #Create function to make a move
    def move(gb, p, inR, inC):
        #gb is gameboard, p is the current player (should be 1 or 2)
        #inR and inC are row and column to play to, respectively

        #Currently won't work if the moves are out of range or if the gameboard is
        #not set up properly.  Also does not check for wins yet.

        #Check if player is valid
        if bool(p==1 or p==2) == False:
            print("Error: Invalid player")
            return(-1)

        #If space is unoccupied, play there
        if (gb.B[inR][inC]==0):
            gb.B[inR][inC] = p
        else:
            print("Error: Space is occupied")
            return(-1)

    #Create a function to display the board
    def disp(gb):
        for r in range(0,gb.N):
            s = repr(int(gb.B[r][0]))
            for c in range(1,gb.N):
                s = s + " " + repr(int(gb.B[r][c]))
            print(s)

################ FUNCTIONS ################


################ Run test cases ################
#Create some objects
G = GameBoard()
print(G.N)
G1 = GameBoard(5)
print(G1.N)
#Make some moves
G.move(1,1,1)
G.move(2,0,1)
G.disp()
