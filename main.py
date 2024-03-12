from nezhaplayer import ChessPlayer
class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.player = ChessPlayer("white")

    def initialize_board(self):
        board = [
            ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜'],
            ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
            ['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖']
        ]
        return board

    def play_game(self):
        while not self.is_game_over():
            self.print_board()
            move = self.player.get_move(self.board)
            self.make_move(move)
        print("Game Over")

    def is_game_over(self):
        pass

    def make_move(self, move):
        print(move)
        initial_row, initial_col = move[0][0], move[0][1]
        final_row, final_col = move[1][0], move[1][1]
        self.board[final_row][final_col] = self.board[initial_row][initial_col]
        self.board[initial_row][initial_col] = ' '
        self.print_board()
        raise
        pass

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        

if __name__ == "__main__":
    game = ChessGame()
    game.play_game()
    print(game)