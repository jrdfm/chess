#!/usr/bin/env python3
# import chess
# import math
# MAXVAL = 10000

# def min_max_move(board, depth):
#     def minimax(board, depth, maximizing_player):
#         if depth == 0 or board.is_game_over():
#             return board.result(), None
        
#         best_value = -MAXVAL if maximizing_player else MAXVAL
#         best_move = None
#         print(f'type {type(best_value)} best_value {best_value}')

#         for move in board.legal_moves:
#             board.push(move)
#             value, _ = minimax(board, depth-1, not maximizing_player)
#             board.pop()
#             print(f'type {type(value)} value {value}')

#             # assert(type(value) == "<class 'float'>")
#             print(f'type {type(best_value)} best_value {best_value}')
#             print(f'type {type(move)} move {move}')

#             print(f'type {type(value)} value {value}')
#             if type(value) != str:
#                 if maximizing_player:
#                     if value > best_value:
#                         best_value = value
#                         best_move = move
#                 else:
#                     if value < best_value:
#                         best_value = value
#                         best_move = move
#             else:
#                 return -MAXVAL, None
#         return best_value, best_move
    
#     _, best_move = minimax(board, depth, True)
    
#     return best_move



# board = chess.Board()

# # make a move
# board.push(min_max_move(board, 5))


import chess
from const import *
import time


def min_max_move(board, depth, alpha, beta):
    best_value = -9999
    best_move = None
    
    for move in board.legal_moves:
        board.push(move)
        value = -min_max(board, depth - 1, -beta, -alpha)
        board.pop()
        
        if value > best_value:
            best_value = value
            best_move = move
            
    return best_move

def min_max(board, depth, alpha, beta):
    if depth == 0 or board.is_checkmate() or board.is_stalemate():
        if board.is_checkmate():
            return -1
        elif board.is_stalemate():
            return 0
        else:
            return evaluate_board(board)
    
    value = -9999
    for move in board.legal_moves:
        board.push(move)
        value = max(value, -min_max(board, depth - 1, -beta, -alpha))
        board.pop()
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value


def evaluate_board(board):
    value = v = 0
    piece_values = [0, 1, 3, 3, 5, 9]

    # start_time = time.time()
    for color in (chess.WHITE, chess.BLACK):
        for piece_type in (chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN):
            value += len(board.pieces(piece_type, color)) * piece_values[piece_type] * [-1,1][color]
    # print(time.time() - start_time)
    # start_time = time.time()
    # for p in board.piece_map().values():
    #     v += val[p.symbol()]
        
    # print(time.time() - start_time)
    # ls = []
    # for p in board.piece_map().values():
    #     ls.append(p)
    # print(ls)
    print(v , value)
    return value


board = chess.Board()

# make a move
move = min_max_move(board, 5,-9999, 9999)
print(move)
board.push(move)
