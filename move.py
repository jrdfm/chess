import chess
from const import *

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
