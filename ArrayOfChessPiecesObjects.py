self.chess_pieces = {
    'P': [Pawn("white", self.positionsx[column], self.positionsy[row]) for column in self.positionsx for row in ["2", "7"]],
    'p': [Pawn("black", self.positionsx[column], self.positionsy[row]) for column in self.positionsx for row in ["2", "7"]],
    'R': [Castle("white", self.positionsx['a'], self.positionsy['1']), Castle("white", self.positionsx['h'], self.positionsy['1'])],
    'r': [Castle("black", self.positionsx['a'], self.positionsy['8']), Castle("black", self.positionsx['h'], self.positionsy['8'])],
    'N': [Knight("white", self.positionsx['b'], self.positionsy['1']), Knight("white", self.positionsx['g'], self.positionsy['1'])],
    'n': [Knight("black", self.positionsx['b'], self.positionsy['8']), Knight("black", self.positionsx['g'], self.positionsy['8'])],
    'B': [Bishop("white", self.positionsx['c'], self.positionsy['1']), Bishop("white", self.positionsx['f'], self.positionsy['1'])],
    'b': [Bishop("black", self.positionsx['c'], self.positionsy['8']), Bishop("black", self.positionsx['f'], self.positionsy['8'])],
    'Q': [Queen("white", self.positionsx['d'], self.positionsy['1'])],
    'q': [Queen("black", self.positionsx['d'], self.positionsy['8'])],
    'K': [King("white", self.positionsx['e'], self.positionsy['1'])],
    'k': [King("black", self.positionsx['e'], self.positionsy['8'])]
}
self.chess_pieces_emoji = {
    "R": '♜', "N": '♞', "B": '♝', "Q": '♛', "K": '♚', "P": '♟',
    "r": '♖', "n": '♘', "b": '♗', "q": '♕', "k": '♔', "p": '♙'
}
