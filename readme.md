# Chess AI Project

This Chess AI project is a versatile chess engine developed in Python. It is capable of various play modes and employs advanced algorithms to provide a challenging chess-playing experience. The project highlights include:

## Features

- Supports two-player mode, self-play, and playing against the computer.
- Implements the minimax algorithm enhanced by alpha-beta pruning for efficient move generation and decision-making.
- Utilizes Monte Carlo Tree Search (MCTS) for improved decision-making, especially in positions with high branching factors.
- Incorporates the Stockfish chess engine for advanced gameplay analysis and evaluation.

## Project Structure

The project is organized as follows:

- `main.py`: The main Python script containing the entry point of the chess engine and gameplay initialization.
- `board.py`: Module for managing the chessboard state and legal moves.
- `dragger.py`: Module for handling player input and piece dragging (if applicable).
- `move.py`: Module for move generation and validation.
- `game.py`: Module for managing the game loop and player interactions.
- `monte_carlo.py`: Module containing the Monte Carlo Tree Search (MCTS) implementation.
- `min_max.py`: Module containing the minimax algorithm with alpha-beta pruning.
- `piece.py`: Module for defining chess piece types and behavior.
- `const.py`: Module for defining constants used throughout the project.
- `test.py`: Module containing unit tests for the chess engine.
- `play.py`: Module for different play modes, including two-player mode, self-play, and playing against the computer.
- `img/`: Directory containing image assets for the chessboard and pieces.


## Usage

To use the Chess AI in your Python projects or play chess:

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/chess-ai.git
   cd chess-ai
   ```

In play.py in the play class edit the players as such.
use player.stock_move() for stockfish engine, player.engine_move() for min_max engine or player.rand_player_move() for random player. And just run:


   ```bash
   ./main.py
   ```

Note: add GUI menu for choosing mode
