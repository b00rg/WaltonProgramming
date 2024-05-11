# put the chess pieces into a queen's gambit
# prints "Password" onto the screen
# change password to the password to the combination lock

class ChessPiece:
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
        pass # input your legal move statement here

class King(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
        if abs(self.xpos - movingxpos) <= 1 and abs(self.ypos - movingypos) <= 1:
            return True
        return False

class Queen(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
        pass # input your legal move statement in here
        
class Knight(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
        pass  # input your legal move statement in here

class ChessBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.populate_board()

    def populate_board(self):
        # Populate pawns
        for i in range(8):
            self.board[1][i] = Pawn("black", i, 1)  
            self.board[6][i] = Pawn("white", i, 6)  
    
        # Populate other pieces
        self.board[0][0] = Castle("black", 0, 0)
        self.board[0][7] = Castle("black", 0, 7)
        self.board[7][0] = Castle("white", 7, 0)
        self.board[7][7] = Castle("white", 7, 7)
        
        self.board[0][1] = Knight("black", 0, 1)
        self.board[0][6] = Knight("black", 0, 6)
        self.board[7][1] = Knight("white", 7, 1)
        self.board[7][6] = Knight("white", 7, 6)
        
        self.board[0][2] = Bishop("black", 0, 2)
        self.board[0][5] = Bishop("black", 0, 5)
        self.board[7][2] = Bishop("white", 7, 2)
        self.board[7][5] = Bishop("white", 7, 5)
        
        self.board[0][3] = Queen("black", 0, 3)
        self.board[7][3] = Queen("white", 7, 3)
        
        self.board[0][4] = King("black", 0, 4)
        self.board[7][4] = King("white", 7, 4)

    def print_board(self):
        piece_emojis = {
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
        column_labels = "ABCDEFGH"
        print("  ", " ".join(column_labels))
        for i, row in enumerate(self.board):
            print(i+1, end="  ")
            for piece in row:
                if piece:
                    piece_name = piece.__class__.__name__ + "_" + piece.colour
                    print(piece_emojis[piece_name], end=' ')
                else:
                    print('_', end=' ')
            print()

    def move_piece(self, startx, starty, endx, endy):
        print("Moving piece from", startx, starty, "to", endx, endy)  # Debugging print
        piece = self.board[starty][startx]
        if not piece:
            print("No piece at the given position.")
            return False
                
        if piece.legalMove(endx, endy, self.board):  # Passing the board instance
            self.board[endy][endx] = piece
            self.board[starty][startx] = None
            piece.xpos = endx
            piece.ypos = endy
            print("Moved", piece.__class__.__name__, "to", endx, endy)  # Debugging print
            return True
        else:
            print("Illegal move.")
            return False

# Game Loop
def play_chess():
    board = ChessBoard()
    player = 1
    while True:
        print("Player", player, "'s turn")
        board.print_board()
        start = input("Enter starting position (e.g., A2): ").upper()
        end = input("Enter ending position (e.g., A4): ").upper()
        startx, starty = ord(start[0]) - ord('A'), int(start[1]) - 1
        endx, endy = ord(end[0]) - ord('A'), int(end[1]) - 1
        if 0 <= startx <= 7 and 0 <= starty <= 7 and 0 <= endx <= 7 and 0 <= endy <= 7:
            if board.move_piece(startx, starty, endx, endy):
                player = 3 - player  # Switch players
            else:
                print("Try again.")
        else:
            print("Invalid coordinates. Coordinates must be within the board.")
        if isinstance(board.board[3][3], Pawn) and board.board[3][3].colour == "black":
            if isinstance(board.board[4][2], Pawn) and board.board[4][2].colour == "white":
                if isinstance(board.board[4][3], Pawn) and board.board[4][3].colour == "white":
                    print("Password")

play_chess()
