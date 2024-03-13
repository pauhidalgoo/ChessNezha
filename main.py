from nezhaplayer import ChessPlayer
import time
class ChessGame:
    def __init__(self):
        self.board = self.initialize_board()
        self.player = ChessPlayer("white")
        self.player2 = ChessPlayer("black")
        self._enpassant = True
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
            if self.is_game_over():
                break
            move = self.player2.get_move(self.board)
            self.make_move(move)
            time.sleep(0.1)

        print("Game Over. " + self.is_game_over() + " has won.")

    def is_game_over(self):
        black = False
        white = False
        for row in self.board:
            for piece in row:
                if piece == '♔':
                    black = True
                    if white:
                        return False
                if piece == '♚':
                    white = True
                    if black:
                        return False
        if black:
            return "Black"
        else:
            return "White"

    def make_move(self, move):
        initial_row, initial_col = move[0][0], move[0][1]
        final_row, final_col = move[1][0], move[1][1]
        if self.board[final_row][final_col] != ' ':
            print(self.board[initial_row][initial_col] + "  killed "+ self.board[final_row][final_col])
        self.board[final_row][final_col] = self.board[initial_row][initial_col]
        self.board[initial_row][initial_col] = ' '
        if len(move) == 4:
            initial_rook_row, initial_rook_col = move[2][0], move[2][1]
            final_rook_row, final_rook_col = move[3][0], move[3][1]
            self.board[final_rook_row][final_rook_col] = self.board[initial_rook_row][initial_rook_col]
            self.board[final_rook_row][initial_rook_col] = ' '
            print("Castled")
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