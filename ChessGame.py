# this is the barebones of the chess game code
# it will NOT work by itself; your task is to finish the rest of the code

import math  # this is 

# this is the barebones of the chess game code
# it will NOT work by itself; your task is to finish the rest of the code

import math  # this is 

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
        if abs(movingxpos - self.xpos) == abs(movingypos - self.ypos):
            return True
        return False


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
        if abs(movingxpos - self.xpos) == abs(movingypos - self.ypos):
            return True
        if (self.xpos == movingxpos or self.ypos == movingypos):
            return True 
        return False

        
class Knight(ChessPiece):
    def __init__(self, colour, xpos, ypos):
        super().__init__(colour, xpos, ypos)

    def legalMove(self, movingxpos, movingypos, board):
        if (self.xpos - movingxpos == 3 or movingxpos-self.xpos == 3) and (self.ypos - movingypos == 2 or movingypos-self.ypos == 2):
            return True
        elif (self.ypos - movingypos == 3 or movingypos-self.ypos == 3) and (self.xpos - movingxpos == 2 or movingxpos-self.xpos == 2):
            return True
        return False
    
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

# This bit here is the mathematical function minmax to create an ai chess player, to call later in the play_chess() function
# I have implemented this already in the play_chess function, so no additional code is needed for the ai. 
# Unfortunately, we won't have time to cover how this works in this module, but if you are interested, check out this video:
# https://www.youtube.com/watch?v=l-hh51ncgDI&ab_channel=SebastianLague
class MinimaxChessPlayer:
    def __init__(self, colour):
        self.colour = colour

    def get_legal_moves(self, board):
        legal_moves = []
        for y in range(8):
            for x in range(8):
                piece = board[y][x]
                if piece and piece.colour == self.colour:
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if dy == 0 and dx == 0:
                                continue
                            new_x, new_y = x + dx, y + dy
                            if 0 <= new_x < 8 and 0 <= new_y < 8:
                                if piece.legalMove(new_x, new_y, board):
                                    legal_moves.append(((x, y), (new_x, new_y)))
        return legal_moves

    def simulate_move(self, board, move):
        start, end = move
        new_board = [row[:] for row in board]
        x, y = start
        new_x, new_y = end
        new_board[new_y][new_x] = new_board[y][x]
        new_board[y][x] = None
        return new_board

    def evaluate_board(self, board):
        # Simple evaluation function: count pieces
        score = 0
        for row in board:
            for piece in row:
                if piece:
                    if piece.colour == self.colour:
                        score += self.get_piece_value(piece)
                    else:
                        score -= self.get_piece_value(piece)
        return score

    def get_piece_value(self, piece):
        # Assign values to pieces for evaluation
        if isinstance(piece, Pawn):
            return 1
        elif isinstance(piece, Knight) or isinstance(piece, Bishop):
            return 3
        elif isinstance(piece, Castle):
            return 5
        elif isinstance(piece, Queen):
            return 9
        elif isinstance(piece, King):
            return 1000  # Arbitrarily high value for the king
        return 0

def ai_move(board, ai_player):
    legal_moves = ai_player.get_legal_moves(board)
    best_move = None
    best_score = -math.inf
    for move in legal_moves:
        new_board = ai_player.simulate_move(board, move)
        score = ai_player.evaluate_board(new_board)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move
    
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

        # AI player's turn 
        # ignore this piece of code here; it calles the ai chess player to move and switches the players
        # you need only concern yourself with the human player in this chess game
        ai_best_move = ai_move(board.board, ai_player)
        if ai_best_move:
            start, end = ai_best_move
            startx, starty = start
            endx, endy = end
            if board.move_piece(startx, starty, endx, endy):
                player = 3 - player  # Switch players
            else:
                print("AI made an invalid move. Game ends.")
                break
        else:
            print("AI cannot make a move. Game ends.")
            break

play_chess() # calling the play chess function

