class Castle(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)
    
    def legalMove(self, movingxpos, movingypos):
        if (self.xpos == movingxpos or self.ypos == movingypos):
            return True 
        return False

castle_instance = Castle("black", 2, 4)
print(castle_instance.legalMove(2, 6)) # True
print(castle_instance.legalMove(3, 6)) # False
