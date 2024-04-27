class ChessPiece:
    def __init__(self, colour, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour

class Pawn(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)
        self.firstMove = True

    def legalMove(self, movingxpos, movingypos):
        if self.colour == "black":
            if self.firstMove and movingypos - self.ypos == 2 and movingxpos == self.xpos:
                self.firstMove = False
                return True
            elif movingypos - self.ypos == 1 and movingxpos == self.xpos:
                if self.firstMove = True:
                    self.firstMove = False
                return True
            
        elif self.colour == "white":
            if self.firstMove and self.ypos - movingypos == 2 and movingxpos == self.xpos:
                self.firstMove = False
                return True
            elif self.ypos - movingypos == 1 and movingxpos == self.xpos:
                return True
        return False

pawn_instance = Pawn("black", 2, 4)
print(pawn_instance.legalMove(2, 6)) # True
print(pawn_instance.legalMove(3, 6)) # False
