# this is the barebones of the chess game code
# it will NOT work by itself; your task is to finish the rest of the code

class ChessPiece:
    def __init__(self, colour, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour

class Pawn(ChessPiece): # logic for Pawn is changed to work with diagonal capturing of pieces
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
            return False

        if movingxpos == self.xpos and movingypos == self.ypos + direction:
            return True
        elif (not self.has_moved and movingxpos == self.xpos and movingypos == self.ypos + 2 * direction and 
              board[self.ypos + direction][self.xpos] is None and
              board[self.ypos + 2 * direction][self.xpos] is None):
            return True
        # Pawns can capture diagonally
        elif (abs(movingxpos - self.xpos) == 1 and movingypos - self.ypos == direction and
              board[movingypos][movingxpos] is not None):
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

    def legalMove(self, movingxpos, movingypos):
      pass # put in your logic here

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)] # initialise the board list to null 
        self.populate_board()  # call for the initialisation of the board

    def populate_board(self):
        # Populate pawns
        for i in range(8):
            self.board[1][i] = Pawn("black", i, 1)  
            self.board[6][i] = Pawn("white", i, 6)  
    
        # Populate other pieces
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
            pass # implement logic for if there is no piece at the starting position here
        if piece.legalMove(endx, endy, self.board):  # Passing the board instance
            pass # implement logic to move piece here
        else:
            pass # implement logic if not legal move here

# Game Loop
def play_chess():
    board = ChessBoard()
    player = 1
    while True:
      # put game loop logic here
      # have the players change turn each iteration of the loop
      # print the board each time
      # have the player input their starting position and ending position, to input into the `move_piece` function
      # also check if the move is invalid and let the user know if their move is invalid, and to try inputting their move again

play_chess() # calling the play chess function
