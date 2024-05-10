# this is the barebones of the chess game code
# it will NOT work by itself; your task is to finish the rest of the code

class ChessPiece: ≈
    def __init__(self, colour, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour

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

class Castle(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)
    
    def legalMove(self, movingxpos, movingypos, board):
        if (self.xpos == movingxpos or self.ypos == movingypos):
            return True 
        return False

class Bishop(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)
    
    def legalMove(self, movingxpos, movingypos, board):
      pass

class King(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
      pass # put in your logic here

class Queen(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
      pass # put in your logic here
        
class Knight(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
      pass # put in your logic here

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] # initialise the board list to null 
        self.populate_board()  # call for the initialisation of the board

    def populate_board(self):
        self.board[0][0] = Castle("black", 0, 0)
        # Place the rest of the pieces in the chess board initialisation here

    def print_board(self):
        piece_emojis = { # dictionary to access the emoji pieces of the chess piece 
            "Pawn_black": "♟️",
            "Pawn_white": "♙",
            "Castle_black": "♜",
            "Castle_white": "♖",
            "Knight_black": "♞",
            "Knight_white": "♘",
            "Bishop_black": "♝",
            "Bishop_white": "♗",
            "Queen_black": "♛",
            "Queen_white": "♕",
            "King_black": "♚",
            "King_white": "♔"
        }
        # have the board print logic here

    def move_piece(self, startx, starty, endx, endy):
        piece = self.board[starty][startx]
        if not piece:
            # have print statement here to inform the player of the legality of their move
            return False # no piece in given position
        if piece.legalMove(endx, endy, self.board):  # Passing the board instance
            pass # implement logic to move piece here
            # change array of objects of chess board to current positionn
            # change the draw board logic to update to current position
            # end position of piece = current position of piece
            # start position of piece = empty
            return True # chess piece is allowed to move into given position
        else:
            # have print statement here to inform the player of the legality of their move
            return False # not legal move

# Game Loop
def play_chess():
    board = ChessBoard()
    player = 1 
    while True:
      # have the players change turn each iteration of the loop, printing which player is playing each time 
      # print the board each time
      # have the player input their starting position and ending position
      # change the inputted values, e.g. A2 -> [0, 1] to input into the move_piece function
      # also check if the move is within the bounds of the chess board
      # let the user know if their move is invalid if false, and to try inputting their move again using a print statement
      # have a correct termination of the game, i.e. when the king is taken 
      # have an end game print statement

play_chess() # calling the play chess function
