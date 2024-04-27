class Pawn(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)  # inheriting the initialisation from the Chess Piece class
        self.firstMove = True # checking if the pawn has moved yet; note this is only relevant for the pawn class and not other chess pieces 

    def legalMove(self, movingxpos, movingypos): # here, we define a function which returns True if the move we input as movingxpos and movingypos is legal in the game of chess, and False if not
        if self.colour == "black": # note that again, this is only relevant for the pawn class and not other chess pieces
            if self.firstMove and movingypos - self.ypos == 2 and movingxpos == self.xpos: # if the difference between the ypos we want to move into and the current ypos is 2, with the xpos staying the same, return true (moving 2 up)
                self.firstMove = False # setting the first move to false after moving for the first time 
                return True # return true if the above statements are true
            elif movingypos - self.ypos == 1 and movingxpos == self.xpos: # if the difference between the ypos we want to move into and the current ypos is 1, with the xpos staying the same, return true (moving 1 up)
                if self.firstMove = True:
                    self.firstMove = False
                return True
            
        elif self.colour == "white":  # same as for a black pawn, but in the opposite directions
            if self.firstMove and self.ypos - movingypos == 2 and movingxpos == self.xpos:
                self.firstMove = False 
                return True
            elif self.ypos - movingypos == 1 and movingxpos == self.xpos:
                return True
        return False # if none of the above statements are true, default to the return False

pawn_instance = Pawn("black", 2, 4) # creating a pawn instance to check if the legalMove function works
print(pawn_instance.legalMove(2, 6)) # prints True
print(pawn_instance.legalMove(3, 6)) # prints False
