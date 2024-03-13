# Nezha Chess Player

This repository contains a simple implementation of chess in Python. This implementation includes a simple (right now) AI bot to play against.

## Installation and usage

To use it you need to have installed Python (I use 3.11). To play the game, simply run the `main.py` file.

The game will start. If you don't change anything, two bots will play aganist each other. To change this, create the game with human=True. You will be prompted to make moves using coordinates (row, column) e.g. '1,1 1,2'. The game will continue until the king is dead (currently it still doesn't check checkmates beforehand, so take that into account).

## Gameplay

- The board is displayed in the console, with pieces represented by Unicode characters.
- Players take turns making moves.
- The game checks for valid moves and enforces the rules of chess.
- Special moves such as castling and en passant are supported.
- The game ends when one player kills the other king.

## Structure

- `main.py`: Defines the `ChessGame` class, which manages the game state and logic.
- `nezha_player.py`: Implements a simple AI player.
- `README.md`: Provides information about the repository.

## Credits

This chess game is developed by Pau Hidalgo Pujol :)