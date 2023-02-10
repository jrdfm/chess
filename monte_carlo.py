import random
import time
import copy

def monte_carlo_tree_search(board, simulations):
    new_board = copy.deepcopy(board)
    start_time = time.time()

    def simulate_random_game(new_board):
        while not new_board.is_game_over():
            move = random.choice(list(new_board.legal_moves))
            new_board.push(move)

        return new_board.result()

    move_wins = {}
    move_plays = {}

    for move in new_board.legal_moves:
        move_wins[move] = 0
        move_plays[move] = 0

    for i in range(simulations):
        board_copy = new_board.copy()
        board_copy.push(random.choice(list(board_copy.legal_moves)))

        winner = simulate_random_game(board_copy)
        for move in board_copy.move_stack:
            if winner == "1-0":
                move_wins[move] += 1
            move_plays[move] += 1

    best_move = max(new_board.legal_moves, key=lambda move: move_wins.get(move, 0) / move_plays.get(move, 1))
    print("Best move: ", best_move)
    print("Simulations: ", simulations)
    print("Time taken: ", time.time() - start_time, " seconds")
    return best_move
