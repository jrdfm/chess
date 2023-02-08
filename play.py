from tkinter import E
import chess
import chess.engine
import pygame
import random
import traceback
from const import *
from min_max import *



class Player(object):
    def __init__(self, board, color ,engine = None):
        self._board = board.board
        self.b = board.b
        self.color  = color
        self._engine = engine
        self.init_stockfish()

    def init_stockfish(self):
        print('init')
        self.engine = True
        try:
            self.__engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
            return True
        except Exception:
            return False

    # def move(self, piece, move):
    #     i, f = move
    #     uci = Move(i, f).to_uci()
    #     # push move
    #     self.board.push(chess.Move.from_uci(uci))
        
    #     # update board
    #     i_row, i_col = i
    #     f_row, f_col = f
    #     self.b[i_row][i_col] = None
    #     self.b[f_row][f_col] = piece

    
    def engine_move(self):
     
        result = self.__engine.play(self._board, chess.engine.Limit(time= 0.5))
        move = result.move
        try:
            self._board.push(move)
            i = chess.parse_square(move.uci()[:2])
            f = chess.parse_square(move.uci()[2:])
            c_i = b_to_c[i]
            c_f = b_to_c[f]
            # update board
            i_row, i_col = c_i
            f_row, f_col = c_f

            self.b[f_row][f_col] = self.b[i_row][i_col] 
            self.b[i_row][i_col] = None

            # print(f'engine move {move} uci {move.uci()} type {type(move.uci())} i,f {(i,f)} c_i,c_f {(c_i,c_f)}')
        except Exception:
            print("Cant push move")
            traceback.print_exc()
        return self._board

    def engine_move_(self):
         
        move = min_max_move(self._board, 3,-9999, 9999)
        # print(move)
        try:
            self._board.push(move)
            i = chess.parse_square(move.uci()[:2])
            f = chess.parse_square(move.uci()[2:])
            c_i = b_to_c[i]
            c_f = b_to_c[f]
            # update board
            i_row, i_col = c_i
            f_row, f_col = c_f

            self.b[f_row][f_col] = self.b[i_row][i_col] 
            self.b[i_row][i_col] = None

            # print(f'engine move {move} uci {move.uci()} type {type(move.uci())} i,f {(i,f)} c_i,c_f {(c_i,c_f)}')
        except Exception:
            print("Cant push move")
            traceback.print_exc()
        return self._board
    
    def rand_player_move(self):
        move = random.choice(list(self._board.legal_moves))
        try:
            print(f'rand player move {move}')
            self._board.push(move)
        except Exception:
            print("Cant push move")
        return self._board

    def is_turn(self):
        board = self._board
        return c_b[board.turn] == self.color

class Play:
    def __init__(self, board):
        self.board = board # Board obj
        self._board = board.board
        self.b = board.b # board repr in Board

    def play(self):
        player_1 = Player(self._board, 'w', True)
        player_2 = Player(self._board, 'b',True)
        board = self._board
        move_event = pygame.event.Event(pygame.USEREVENT)
        
        if not board.is_game_over():
            
            if player_1.is_turn():
                board = player_1.rand_player_move()
                pygame.event.post(move_event)

            elif player_2.is_turn():
                print("Hi")
                board = player_2.engine_move_()
                pygame.event.post(move_event)

        else:
            print("GAME IS OVER")
            pygame.event.post(pygame.QUIT)




if __name__ == '__main__':
    pygame.init()
    e = pygame.USEREVENT
    pygame.time.set_timer(e, 3000)
    # for i in range(25):
    #     e = pygame.USEREVENT + i
    #     print(e)
    ADD_event = pygame.event.Event
    pygame.event.post(ADD_event)
    while True:
        for event in pygame.event.get():
            
            if event.type == e:
                print("NULL")

