class ChessPiece: # parent class for all chess pieces; initialises the xpos, ypos and colour
    def __init__(self, colour, xpos, ypos): 
        self.xpos = xpos 
        self.ypos = ypos
        self.colour = colour

