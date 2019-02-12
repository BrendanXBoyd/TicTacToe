"""Player 1 is 1, player 2 is 2.  Each turn, the player inputs which square they want
The square is filled with a 1 or 2 (unless already full)
When there is a completed win, or a full board, the game ends"""

################ Imports ################
import numpy as np

################ CLASSES ################
class GameBoard:
    #Create initialization funtion
    def __init__(gb, boardSize = 3):
        # N stores the size of the game
        # B stores the board itself
        # rWin, cWin, and dWin store the current winners in each row, col, and
        # diagonal, respectively.
        # W stores the game's winner
        # tieCount, when this variable hits 2N+2, the game ends in a tie
        gb.N = boardSize
        gb.B = np.zeros((boardSize,boardSize))
        gb.rWin = np.zeros((boardSize,2))
        gb.cWin = np.zeros((boardSize,2))
        gb.dWin = np.zeros((2,2))
        gb.W = 0
        gb.tieCount = 0

    #Create function to make a move
    #Returns the player (p) if they won, 0 for a tie, or -1 for an error
    def move(gb, p, inR, inC):
        #p is the current player (should be 1 or 2)
        #inR and inC are row and column to play to, respectively

        #Check if player is valid
        if bool(p==1 or p==2) == False:
            print("Error: Invalid player")
            return(-1)

        #Check if move is within bounds
        if (inR < 0 or inR >= gb.N or inC < 0 or inC >= gb.N):
            print("Error: Move is out of bounds")
            return(-1)

        #If space is unoccupied and within bounds, play there
        if (gb.B[inR][inC]==0):
            #Add player to the space
            gb.B[inR][inC] = p
            #Check for a win
            winner = gb.checkWinOrTie(p, inR, inC)
            if (winner != -1): return(winner)
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

    #Function to see if the game is over
    #returns 0 for a tie, p if they won, or -1 if the game continues
    def checkWinOrTie(gb, p, inR, inC):
        ## Check in the row ##
        if (gb.rWin[inR][1] == 0):
            #No one has played in this row yet
            gb.rWin[inR][1] = p
            gb.rWin[inR][0] = 1
        elif (gb.rWin[inR][1] == p):
            #This player is winning in this row
            gb.rWin[inR][0] += 1
            #Check if the player has won in this row
            if (gb.rWin[inR][0] >= gb.N):
                #The player has won, print the winner and return
                print("Player", p, "has won!")
                gb.W = p
                return(p)
        elif (gb.rWin[inR][1] != -1):
            #This player is not winning in this row, so there is no winner
            gb.rWin[inR][1] = -1
            #Increment the tie counter
            gb.tieCount += 1

        ## Check in the column ##
        if (gb.cWin[inC][1] == 0):
            #No one has played in this col yet
            gb.cWin[inC][1] = p
            gb.cWin[inC][0] = 1
        elif (gb.cWin[inC][1] == p):
            #This player is winning in this col
            gb.cWin[inC][0] += 1
            #Check if the player has won in this col
            if (gb.cWin[inC][0] >= gb.N):
                #The player has won, print the winner and return
                print("Player", p, "has won!")
                gb.W = p
                return(p)
        elif (gb.cWin[inC][1] != -1):
            #This player is not winning in this col, so there is no winner
            gb.cWin[inC][1] = -1
            #Increment the tie counter
            gb.tieCount += 1

        ## Check the diagonals ##
        #Check the first diagonal
        if (inR == inC):
            if (gb.dWin[0][1] == 0):
                #No one has played in this diag yet
                gb.dWin[0][1] = p
                gb.dWin[0][0] = 1
            elif (gb.dWin[0][1] == p):
                #The current player is winning in this diag
                gb.dWin[0][0] += 1
                #Check if the player has won in this diag
                if (gb.dWin[0][0] >= gb.N):
                    #The player has won, print the winner and return
                    print("Player", p, "has won!")
                    gb.W = p
                    return(p)
            elif (gb.dWin[0][1] != -1):
                #This player is not winning in this diag, so there is no winner
                gb.dWin[0][1] = -1
                #Increment the tie counter
                gb.tieCount += 1
        #Check the other diagonal
        if ((inR + inC) == (gb.N - 1)):
            if (gb.dWin[1][1] == 0):
                #No one has played in this diag yet
                gb.dWin[1][1] = p
                gb.dWin[1][0] = 1
            elif (gb.dWin[1][1] == p):
                #The current player is winning in this diag
                gb.dWin[1][0] += 1
                #Check if the player has won in this diag
                if (gb.dWin[1][0] >= gb.N):
                    #The player has won, print the winner and return
                    print("Player", p, "has won!")
                    gb.W = p
                    return(p)
            elif (gb.dWin[1][1] != -1):
                #This player is not winning in this diag, so there is no winner
                gb.dWin[1][1] = -1
                #Increment the tie counter
                gb.tieCount += 1
        #Check if the game is tied
        if (gb.tieCount >= (2*gb.N + 2)):
            print("The game is tied")
            gb.W = -1
            return(0)
        #If we've made it this far, the game continues
        return(-1)

################ FUNCTIONS ################


################ Run test cases ################
#Create some objects
G = GameBoard()
print(G.N)
G1 = GameBoard(5)
print(G1.N)
#Make some moves
G.move(1,1,0)
G.move(2,0,1)
G.move(1,0,4)
G.disp()
G1.move(1,1,1)
G1.move(2,0,1)
G1.move(1,0,4)
G1.disp()
#Let player 2 win
G.move(2,1,1)
G.disp()
G.move(2,0,2)
G.disp()
G.move(2,2,0)
G.disp()
