import chess
from const import *


class Board:
    def __init__(self):
        self.board = chess.Board()

    def piece(self, loc):
        try:
            return self.board.piece_at(c_to_b[loc]) 
        except KeyError:
            pass

    def has_piece(self, loc):
        return self.piece(loc) != None

    def get_name(self, loc):
        piece = self.piece(loc)
        if piece != None:
            return t_n[piece.piece_type]
                
    def get_color(self, loc):
        piece = self.piece(loc)
        if piece != None:
            return c_b[piece.color]

        
if __name__ == '__main__':
    b = Board()
    print(b.has_piece((0,87)))
    print(b.get_name((0,87)))
    print(b.get_color((0,87)))

    print(b.has_piece((7,0)))
    print(b.get_name((7,0)))
    print(b.get_color((7,0)))

        