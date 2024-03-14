from nezhaplayer import ChessPlayer
from humanplayer import HumanPlayer
from minimaxplayer import MinimaxPlayer
import time
import random
class ChessGame:
    def __init__(self, human = False, verbose = True):
        self.board = self.initialize_board()
        self.print = verbose
        first = random.choice(["white", "black"])
        if first == "white":
            self.player = MinimaxPlayer("white")
            self.player2 = ChessPlayer("black") if not human else HumanPlayer("black")
        else:
            self.player2 = MinimaxPlayer("black")
            self.player = ChessPlayer("white") if not human else HumanPlayer("white")
        self._enpassant = False
        self.move_history = []
        self.repetition_count = {}
        print("Minimax plays", first)
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
        while not (self.is_game_over() in ["white", "black", "no one"]):
            if self.is_game_over() != False:
                print("Forced move") if self.print else None
                move = self.is_game_over()
            else:
                move = self.player.get_move(self.board)
            if move == None:
                print("Game Over. Stalemate.") if self.print else None
                break
            self.make_move(move)
            self.move_history.append(self.board)
            if self.is_game_over() in ["white", "black", "no one"]:
                break
            elif self.is_game_over() != False:
                print("Forced move") if self.print else None
                move = self.is_game_over()
            else:
                move = self.player2.get_move(self.board)
            if move == None:
                print("Game Over. Stalemate.") if self.print else None
                break
            self.make_move(move)
            self.move_history.append(self.board)
            if self.is_repetition():
                print("Draw by repetition.")
                return "draw"

        if self.is_game_over() != False:
            print("Game Over. " + self.is_game_over() + " has won.") if self.print else None
            return self.is_game_over()
        else:
            return "stalemate"
        
    def is_repetition(self):
        board_state = str(self.board)
        self.repetition_count[board_state] = self.repetition_count.get(board_state, 0) + 1
        return self.repetition_count[board_state] >= 5
    def is_game_over(self):
        black_king = None
        white_king = None
        other_pieces = None
        for row_id, row in enumerate(self.board):
            for col_id, piece in enumerate(row):
                if piece == '♔':
                    black_king = (row_id, col_id)
                elif piece == '♚':
                    white_king = (row_id, col_id)
                elif piece != ' ':
                    other_pieces = True
        if other_pieces == None:
            return "no one"
        if black_king == None:
            return "white"
        if white_king == None:
            return "black"
        if self.is_in_check(black_king, 'black'):
            checkmate = self.is_checkmate(black_king, 'black')
            if checkmate[0]:
                return "white"
            else:
                return checkmate[1]
        elif self.is_in_check(white_king, 'white'):
            checkmate = self.is_checkmate(white_king, 'white')
            if checkmate[0]:
                return "black"
            else:
                return checkmate[1]
        return False

    def is_in_check(self, king_position, color):
        play = self.player if self.player.color != color else self.player2
        legal_moves = play.get_available_moves(self.board)
        capturing_moves = []
        if legal_moves:
            capturing_moves = [move for move in legal_moves if play.is_capture(self.board, move) and move[1] == king_position]
        return len(capturing_moves) > 0

    def is_checkmate(self, king_position, color):
        temp_board = [row[:] for row in self.board]
        player = self.player if self.player.color == color else self.player2
        legal_moves = player.get_available_moves(temp_board)
        for move in legal_moves:
            temp_board = [row[:] for row in self.board]
            initial_pos, final_pos = move[0], move[1]
            temp_board[final_pos[0]][final_pos[1]] = temp_board[initial_pos[0]][initial_pos[1]]
            temp_board[initial_pos[0]][initial_pos[1]] = ' '
            new_king_position = king_position if temp_board[king_position[0]][king_position[1]] != ' ' else (final_pos[0], final_pos[1])
            
            play = self.player if self.player.color != color else self.player2
            legal_moves = play.get_available_moves(temp_board)
            capturing_moves = []
            if legal_moves:
                capturing_moves = [move for move in legal_moves if play.is_capture(temp_board, move) and move[1] == new_king_position]
            if len(capturing_moves) == 0:
                return False, move
        return True, None

    def make_move(self, move):
        print(move) if self.print else None
        initial_row, initial_col = move[0][0], move[0][1]
        final_row, final_col = move[1][0], move[1][1]
        if self.board[final_row][final_col] != ' ':
            print(self.board[initial_row][initial_col] + "  killed "+ self.board[final_row][final_col]) if self.print else None

        self.board[final_row][final_col] = self.board[initial_row][initial_col]

        if self._enpassant != False and (final_row,final_col) == self._enpassant[0]:
            print(self.board[initial_row][initial_col] + "  killed by en passant "+ self.board[self._enpassant[1][0]][self._enpassant[1][1]]) if self.print else None
            self.board[self._enpassant[1][0]][self._enpassant[1][1]] = ' '

        self.board[initial_row][initial_col] = ' '

        if len(move) == 4: # Castling
            initial_rook_row, initial_rook_col = move[2][0], move[2][1]
            final_rook_row, final_rook_col = move[3][0], move[3][1]
            self.board[final_rook_row][final_rook_col] = self.board[initial_rook_row][initial_rook_col]
            self.board[initial_rook_row][initial_rook_col] = ' '
            print("Castled") if self.print else None

        if len(move) == 3: # Save for en passant
            self._enpassant = (move[2], move[1])
        else:
            self._enpassant = False
        
        if self.board[final_row][final_col] == "♙" and final_row == 0:
            print("you can promote!") if self.print else None
            self.board[final_row][final_col] = "♕"
        if self.board[final_row][final_col] == "♟" and final_row == 7:
            print("you can promote!") if self.print else None
            self.board[final_row][final_col] = "♛"
        self.print_board()
        print("----------------") if self.print else None
        pass

    def print_board(self):
        for row in self.board:
            print(" ".join(row)) if self.print else None if self.print else None
        

if __name__ == "__main__":
    game = ChessGame()
    game.play_game()
    print("White player was", game.player.__class__)
    """
    for i in range(100):
        random.seed(i)
        print("Iteration ",i)
        game = ChessGame(print=False)
        print(game.play_game())
    """