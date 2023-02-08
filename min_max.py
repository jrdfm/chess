import chess
from const import *


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

    for color in (chess.WHITE, chess.BLACK):
        for piece_type in (chess.PAWN, chess.KNIGHT, chess.BISHOP, chess.ROOK, chess.QUEEN):
            value += len(board.pieces(piece_type, color)) * piece_values[piece_type] * [-1,1][color]

    # print(value)
    return value
