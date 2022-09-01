from re import I
import chess
from const import *
from piece import *

class Board:
    def __init__(self):
        self.board = chess.Board()
        self.b = [[None for _ in range(COLS)] for _ in range(ROWS)]
        self._create()
        self.set_moves()

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                pos = (row,col)
                if self.has_piece(pos):
                    self.b[row][col] = Piece(self.get_name(pos), self.get_color(pos))

    def piece(self, pos):
        try:
            return self.board.piece_at(c_to_b[pos]) 
        except KeyError:
            pass

    def has_piece(self, pos):
        if self.valid(pos):    
            return self.piece(pos) != None

    def get_name(self, pos):
        piece = self.piece(pos)
        if piece != None:
            return t_n[piece.piece_type]
                
    def get_color(self, pos):
        piece = self.piece(pos)
        if piece != None:
            return c_b[piece.color]

    def get_piece(self, pos):
        if self.has_piece(pos):
            row, col = pos
            return self.b[row][col]

    # def get_piece(self, pos):
    #     if self.has_piece(pos):
    #         name = self.get_color(pos)
    #         color = self.get_name(pos)
    #         return  Piece(name, color) 
                    

    def valid(self, pos):
        r, c = pos
        return (0 <= r and r <= 7) and (0 <= c and c <= 7) 

    def set_moves(self):
        for m in self.board.legal_moves:
            i = chess.parse_square(m.uci()[:2])
            f = chess.parse_square(m.uci()[2:])
            pos =  b_to_c[i] #(row,col)
            if self.has_piece(pos):
                self.get_piece(pos).valid_moves.append(b_to_c[f])

    def update_moves(self, piece):
        for m in self.board.legal_moves:
            i = chess.parse_square(m.uci()[:2])
            f = chess.parse_square(m.uci()[2:])
            pos =  b_to_c[i] #(row,col)
            if self.has_piece(pos) and self.get_piece(pos).moved:
                self.get_piece(pos).valid_moves.append(b_to_c[f])





    def get_moves(self, pos):
        pass


    def move(self, piece, move):
        i = move.i # (row, col)
        f = move.f
        # m = chess.Move.from_uci('e7e5')
        # board.push(m)

        self.b[i.row][i.col].piece = None
        self.b[f.row][f.col].piece = piece


class Move:
    def __init__(self, initial, final):
        self.i = initial
        self.f = final
    def to_uci(self):
        to_str = chess.square_name
        i, f  = c_to_b[self.i], c_to_b[self.f]
        return f'{to_str(i)}{to_str(f)}'

    def __eq__(self, other):
        return self.i == other.i and self.f == other.f


if __name__ == '__main__':
    b = Board()
    m = Move((7,0),(0,7))
    # print(b.has_piece((0,87)))
    # print(b.get_name((0,87)))
    # print(b.get_color((0,87)))

    # print(b.has_piece((7,0)))
    # print(b.get_name((7,0)))
    # print(b.get_color((7,0)))

    # # print(b.valid((0,0)))
    # print(f'{b.get_piece((7,0))}')
    print(m.to_uci())
