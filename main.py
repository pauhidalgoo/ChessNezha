from nezhaplayer import ChessPlayer
import time
class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.player = ChessPlayer("white")
        self.player2 = ChessPlayer("black")

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
        self.print_board()
        while not self.is_game_over():
            move = self.player.get_move(self.board)
            self.make_move(move)
            time.sleep(1)
            move = self.player2.get_move(self.board)
            self.make_move(move)
            time.sleep(1)

        print("Game Over")

    def is_game_over(self):
        pass

    def make_move(self, move):
        print(move)
        initial_row, initial_col = move[0][0], move[0][1]
        final_row, final_col = move[1][0], move[1][1]
        if self.board[final_row][final_col] != ' ':
            print(self.board[initial_row][initial_col] + "  killed "+ self.board[final_row][final_col])
        self.board[final_row][final_col] = self.board[initial_row][initial_col]
        self.board[initial_row][initial_col] = ' '
        self.print_board()
        print("----------------")
        pass

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        

if __name__ == "__main__":
    game = ChessGame()
    game.play_game()
    print(game)