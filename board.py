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
        self.last_move = None

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


    def valid(self, pos):
        r, c = pos
        return (0 <= r and r <= 7) and (0 <= c and c <= 7) 

    def set_moves(self):
        for m in self.board.legal_moves:
            try:
                i = chess.parse_square(m.uci()[:2])
                f = chess.parse_square(m.uci()[2:])
                pos =  b_to_c[i] #(row,col)
                if self.has_piece(pos):
                    self.get_piece(pos).valid_moves.append(b_to_c[f])
            except ValueError:
                pass

    def update_moves(self, piece, move):
        for row in range(ROWS):
            for col in range(COLS):
                cur_piece = self.b[row][col]
                if cur_piece != None and piece.color == cur_piece.color and (move in cur_piece.valid_moves):
                    cur_piece.valid_moves.remove(move)




    def is_legal(self, move):
        ini, fin = move
        if ini != fin:
            uci = Move(ini, fin).to_uci()
            return self.board.is_legal(chess.Move.from_uci(uci))
        else:
            return False

    def move(self, piece, move):
        i, f = move
        uci = Move(i, f).to_uci()
        # push move
        self.board.push(chess.Move.from_uci(uci))
        
        # update board
        i_row, i_col = i
        f_row, f_col = f
        self.b[i_row][i_col] = None
        self.b[f_row][f_col] = piece
        self.last_move = move
        piece.valid_moves = []
        self.update_moves(piece, (f_row, f_col)) # remove moved to pos from friends valid
        self.set_moves() # update enemy moves
        

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
