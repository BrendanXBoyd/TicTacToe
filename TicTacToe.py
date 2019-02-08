

#Player 1 is 1, player 2 is 2.  Each turn, the player inputs which square they want
#The square is filled with a 1 or 2 (unless already full)
#When there is a completed win, or a full board, the game ends

################ FUNCTIONS ################

#Create a function to make a move
def makeMove(gb, p, inR, inC):
    #gb is gameboard, p is the current player (should be 1 or 2)
    #inR and inC are row and column to play to, respectively

    #Check if player is valid
    if bool(p==1 or p==2) == False:
        print("Error: Invalid player")
        return(-1)

    #If space is unoccupied, play there
    if (gb[inR][inC]==0):
        gb[inR][inC] = p
    else:
        print("Error: Space is occupied")
        return(-1)

#Create a function to display the board


################ Run test cases ################ 
#Create array to store board
gb = [[0,0,0], [0,0,0], [0,0,0]]

#Make some moves
makeMove(gb, 3, 0, 0)
makeMove(gb, 1, 0, 0)
makeMove(gb, 1, 0, 0)
