class Pawn(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)
        self.has_moved = False  # Track if the pawn has moved

    def legalMove(self, movingxpos, movingypos, board):
        # Pawns can move forward one square, or two squares on their first move
        if self.colour == "black":
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6
        
        # Check if the destination square is within bounds
        if movingxpos < 0 or movingxpos > 7 or movingypos < 0 or movingypos > 7:
            return False

        # Check if the destination square is occupied
        if board[movingypos][movingxpos] is not None:
            # If the destination square is occupied by an opponent's piece, allow capturing
            if board[movingypos][movingxpos].colour != self.colour:
                return abs(movingxpos - self.xpos) == 1 and movingypos - self.ypos == direction
            else:
                return False

        if movingxpos == self.xpos and movingypos == self.ypos + direction:
            return True
        elif (not self.has_moved and movingxpos == self.xpos and movingypos == self.ypos + 2 * direction and 
              board[self.ypos + direction][self.xpos] is None and
              board[self.ypos + 2 * direction][self.xpos] is None):
            return True
        
        return False
