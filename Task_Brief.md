1. **Complete Chess Piece Classes, if not already completed**
    * See exercise from week 2 for more information
    * All of the chess pieces must be completed before moving onto the next task
    * Note the `pawn` class and `castle` class has been updated. 
    * The `castle` class can also be found in the walton-programming sample code. 
2. **ChessBoard Class:**
    * Constructor (`__init__` method):
        * Write the `__init__` method for the ChessBoard class.
        * Initialise the board attribute as an 8x8 grid list with all elements set to None. 
    * populate_board Method:
        * Implement the populate_board method to place the initial set of chess pieces on the board.
        * Add the following pieces to their respective starting positions:
            * 8 pawns for each player (placed on the 2nd and 7th ranks).
            * 2 rooks, knights, bishops, and a queen for each player (placed on the 1st and 8th ranks).
            * 1 king for each player (placed on the 1st and 8th ranks).
    * print_board Method:
        * Implement the print_board method to display the current state of the chessboard.
        * Print the board as an 8x8 grid with pieces (you may use the dictionary found in pieces_emojis.py to do this).
        * Include row and column labels to make it easier for players to identify positions (A, B, C, etc. for the rows, and 1, 2, 3, etc. for the columns).
3. **`move_piece` Method:**
    * Parameters:
        * `startx, starty`: The coordinates of the piece to be moved.
        * `endx, endy`: The coordinates where the piece will be moved to.
    * Handling Invalid Moves:
        * Before attempting to move the piece, check if the starting position contains a piece belonging to the current player. If not, print a message indicating that there is no piece at the given position.
    * Legal Move Validation:
        * call upon the ChessPiece `isLegalMove()` to ensure that the chess piece is moving in a way that it is supposed to
    * Updating the Board:
        * If the move is legal, update the board to reflect the new position of the piece.
        * Set the destination square to the moving piece and the original square to None.
        * Update the `xpos` and `ypos` attributes of the piece to reflect its new position on the board.
4. **`play_chess` Function:**
    * Game Initialisation:
        * Start the game by creating an instance of the ChessBoard class.
        * Set the initial player (`player`) to 1.
    * Game Loop:
        * Implement the main game loop where players take turns making moves.
        * Inside the while loop, print the current player's turn and display the board using the print_board method.
        * Prompt the player to enter the starting and ending positions for their move.
        * Convert the input positions to coordinates (`startx, starty, endx, endy`) suitable for the `move_piece` method.
    * Switching Players:
        * After a move is made, switch the current player to the other player.
5. **Challenges:**
    * Code en passant
    * Code pawn promotion
