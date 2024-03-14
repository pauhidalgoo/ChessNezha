from nezhaplayer import ChessPlayer
class MinimaxPlayer(ChessPlayer):
    def __init__(self, color):
        super().__init__(color)
        self.color = color
        self._enpassant = False
        self.left_castling= False
        self.right_castling = False
        if self.color== "white":
            self.pieces =  ['♜', '♞', '♝', '♛', '♚','♟']
            self.other_pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
        elif self.color=="black":
            self.pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
            self.other_pieces = ['♜', '♞', '♝', '♛', '♚','♟']
    def get_move(self, board):
        best_move = self.minimax(board, 3, True, float("-inf"), float("inf"))[1]

        if best_move == None:
            return None
        initial_row, initial_col = best_move[0][0], best_move[0][1]
        if self.left_castling or self.right_castling:
            if board[initial_row][initial_col] == '♜':
                if initial_col == 0 and initial_row == 0:
                    self.left_castling = False
                if initial_col == 7 and initial_row == 0:
                    self.right_castling = False
            if board[initial_row][initial_col] == '♖':
                if initial_col == 0 and initial_row == 7:
                    self.left_castling = False
                if initial_col == 7 and initial_row == 7:
                    self.right_castling = False
            if board[initial_row][initial_col] == '♔' or board[initial_row][initial_col] == '♚':
                self.left_castling = False
                self.right_castling = False
        return best_move

    def minimax(self, board, depth, maximizing_player, alpha, beta):
        if depth == 0:
            return self.evaluate_board(board), None
        
        color = "white" if self.pieces == ['♜', '♞', '♝', '♛', '♚','♟'] else "black"
        other_color = "black" if color == "white" else "white"
        if maximizing_player:
            legal_moves = self.get_available_moves(board, self.pieces, color)
            max_eval = float("-inf")
            best_move = None
            for move in legal_moves:
                new_board = self.simulate_move(board, move)
                eval_val = self.minimax(new_board, depth - 1, False, alpha, beta)[0]
                if eval_val > max_eval:
                    max_eval = eval_val
                    best_move = move
                alpha = max(alpha, eval_val)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            legal_moves = self.get_available_moves(board, self.other_pieces, other_color)
            min_eval = float("inf")
            best_move = None
            for move in legal_moves:
                new_board = self.simulate_move(board, move)
                eval_val = self.minimax(new_board, depth - 1, True, alpha, beta)[0]
                if eval_val < min_eval:
                    min_eval = eval_val
                    best_move = move
                beta = min(beta, eval_val)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate_board(self, board):
        piece_values = [5, 3, 3, 9, 100, 1]
        total_evaluation = 0
        for row in board:
            for square in row:
                if square in self.pieces:
                    total_evaluation += piece_values[self.pieces.index(square)]
                elif square != ' ':
                    total_evaluation -= piece_values[self.other_pieces.index(square)]
        return total_evaluation


    def simulate_move(self, board, move):
        temp_board = [row[:] for row in board]
        initial_row, initial_col = move[0][0], move[0][1]
        final_row, final_col = move[1][0], move[1][1]
        temp_board[final_row][final_col] = temp_board[initial_row][initial_col]

        if self._enpassant != False and (final_row,final_col) == self._enpassant[0]:
            temp_board[self._enpassant[1][0]][self._enpassant[1][1]] = ' '

        temp_board[initial_row][initial_col] = ' '

        if len(move) == 4: # Castling
            initial_rook_row, initial_rook_col = move[2][0], move[2][1]
            final_rook_row, final_rook_col = move[3][0], move[3][1]
            temp_board[final_rook_row][final_rook_col] = temp_board[initial_rook_row][initial_rook_col]
            temp_board[initial_rook_row][initial_rook_col] = ' '

        if len(move) == 3: # Save for en passant
            self._enpassant = (move[2], move[1])
        else:
            self._enpassant = False
        
        if temp_board[final_row][final_col] == "♙" and final_row == 0:
            temp_board[final_row][final_col] = "♕"
        if temp_board[final_row][final_col] == "♟" and final_row == 7:
            temp_board[final_row][final_col] = "♛"
        return temp_board
