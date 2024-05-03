4. ChessBoard Class:
    * Constructor (__init__ method):
        * Write the __init__ method for the ChessBoard class.
        * Initialise the board attribute as an 8x8 grid list with all elements set to None. 
    * populate_board Method:
        * Implement the populate_board method to place the initial set of chess pieces on the board.
        * Add the following pieces to their respective starting positions:
            * 8 pawns for each player (placed on the 2nd and 7th ranks).
            * 2 rooks, knights, bishops, and a queen for each player (placed on the 1st and 8th ranks).
            * 1 king for each player (placed on the 1st and 8th ranks).
    * print_board Method:
        * Implement the print_board method to display the current state of the chessboard.
        * Print the board as an 8x8 grid with pieces represented by Unicode symbols or any other suitable representation.
        * Include row and column labels to make it easier for players to identify positions.
5. move_piece Method:
    * Parameter Explanation:
        * startx, starty: The coordinates of the piece to be moved.
        * endx, endy: The coordinates where the piece will be moved to.
    * Handling Invalid Moves:
        * Exercise: Before attempting to move the piece, check if the starting position contains a piece belonging to the current player. If not, print a message indicating that there is no piece at the given position.
    * Legal Move Validation:
        * Exercise: Implement the logic to validate whether the move is legal for the selected piece.
        * Ensure that the move adheres to the rules of chess for the specific piece being moved.
        * You may need to consider factors such as piece movement patterns, obstruction by other pieces, and special rules like castling and en passant.
    * Updating the Board:
        * Exercise: If the move is legal, update the board to reflect the new position of the piece.
        * Set the destination square to the moving piece and the original square to None.
        * Update the xpos and ypos attributes of the piece to reflect its new position on the board.
6. play_chess Function:
    * Game Initialization:
        * Exercise: Start the game by creating an instance of the ChessBoard class.
        * Set the initial player (player) to 1.
    * Game Loop:
        * Exercise: Implement the main game loop where players take turns making moves.
        * Inside the loop, print the current player's turn and display the board using the print_board method.
        * Prompt the player to enter the starting and ending positions for their move.
        * Convert the input positions to coordinates (startx, starty, endx, endy) suitable for the move_piece method.
    * Switching Players:
        * Exercise: After a move is made, switch the current player to the other player.
        * You can achieve this by updating the player variable to the value of 3 - player, which effectively toggles between player 1 and player 2.
