import random
class ChessPlayer:
    def __init__(self, color):
        self.color = color
        if self.color== "white":
            self.pieces =  ['♜', '♞', '♝', '♛', '♚','♟']
            self.other_pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
        elif self.color=="black":
            self.pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
            self.other_pieces = ['♜', '♞', '♝', '♛', '♚','♟']
        else:
            print("The color is incorrect. It must be white or black")
            raise

        self.left_castling= True
        self.right_castling = True
        pass
     
    def get_move(self, board):
        legal_moves = self.get_available_moves(board)
        if legal_moves:
            capturing_moves = [move for move in legal_moves if self.is_capture(board, move)]
            if capturing_moves:
                move = random.choice(capturing_moves)
            else:
                move = random.choice(legal_moves)
        else:
            return None
        initial_row, initial_col = move[0][0], move[0][1]

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
        return move

    def get_legal_moves(self, board, pieces = None, color = None):
        color = self.color if color == None else color
        pieces = self.pieces if pieces == None else pieces
        legal_moves = []
        for row_id, row in enumerate(board):
            for col_id, piece in enumerate(row):
                if piece in pieces:
                    moves = self.get_piece_moves(board, row_id, col_id, color)
                    legal_moves.extend(moves)
        return legal_moves
    
    def get_available_moves(self, board, pieces = None, color = None):
        pieces = self.pieces if pieces == None else pieces
        color = self.color if color == None else color
        legal_moves = self.get_legal_moves(board, pieces, color)
        king_position = None
        for row_id, row in enumerate(board):
            for col_id, piece in enumerate(row):
                if piece == '♔' and piece in pieces:
                    king_position = (row_id, col_id)
                    break
                elif piece == '♚' and piece in pieces:
                    king_position = (row_id, col_id)
                    break
        if king_position == None:
            return []
        final_moves = []
        for move in legal_moves:
            temp_board = [row[:] for row in board]
            initial_pos, final_pos = move[0], move[1]
            temp_board[final_pos[0]][final_pos[1]] = temp_board[initial_pos[0]][initial_pos[1]]
            temp_board[initial_pos[0]][initial_pos[1]] = ' '
            new_king_position = king_position if temp_board[king_position[0]][king_position[1]] != ' ' else (final_pos[0], final_pos[1])
            if not self.check(temp_board, new_king_position):
                final_moves.append(move)
        return final_moves
    
    def check(self, board, king_position):
        play = ChessPlayer("black") if self.color == "white" else ChessPlayer("white")
        play.left_castling = False
        play.right_castling = False
        legal_moves = play.get_legal_moves(board)
        capturing_moves = []
        if legal_moves:
            capturing_moves = [move for move in legal_moves if play.is_capture(board, move) and move[1] == king_position]
        return len(capturing_moves) > 0
    
    def get_piece_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        piece = board[row][col]
        moves = []
        if piece == '♙' or piece == '♟':
            moves.extend(self._get_pawn_moves(board, row, col, color))
        if piece == '♖' or piece == '♜':
            moves.extend(self._get_rock_moves(board, row, col, color))
        if piece == '♗' or piece == '♝':
            moves.extend(self._get_bishop_moves(board, row, col, color))
        if piece == '♕' or piece == '♛':
            moves.extend(self._get_queen_moves(board, row, col, color))
        if piece == '♔' or piece == '♚':
            moves.extend(self._get_king_moves(board, row, col, color))
        if piece == '♘' or piece == '♞':
            moves.extend(self._get_knight_moves(board, row, col, color))
        return moves
    
    def is_capture(self, board, move):
        target_row, target_col = move[1][0], move[1][1]
        target_piece = board[target_row][target_col]
        return target_piece != ' '
    
    def _get_pawn_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        other_pieces = ['♜', '♞', '♝', '♛', '♚','♟'] if color == "black" else ['♖', '♘', '♗', '♕', '♔', '♙']
        moves = []
        if color == "black" and row - 1 >= 0 and board[row - 1][col] == ' ':
            moves.append(((row, col), (row - 1, col)))
        if color == "white" and row + 1 < 8 and board[row + 1][col] == ' ':
            moves.append(((row, col), (row + 1, col)))
        if color == "black" and row == 6 and board[row - 2][col] == ' ' and board[row - 1][col] == ' ':
            moves.append(((row, col), (row - 2, col), (row - 1, col)))
        if color == "white" and row == 1 and board[row + 2][col] == ' ' and board[row + 1][col] == ' ':
            moves.append(((row, col), (row + 2, col), (row + 1, col)))
        if color == "black" and row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] in other_pieces:
            moves.append(((row, col), (row - 1, col - 1)))
        if color == "black" and row - 1 >= 0 and col + 1 < 8 and board[row - 1][col - 1] in other_pieces:
            moves.append(((row, col), (row - 1, col + 1)))

        if color == "white" and row + 1 < 8 and col - 1 >= 0 and board[row + 1][col - 1] in other_pieces:
            moves.append(((row, col), (row + 1, col - 1)))
        if color == "white" and row + 1 < 8 and col + 1 < 8 and board[row + 1][col - 1] in other_pieces:
            moves.append(((row, col), (row + 1, col + 1)))

        if color == "black" and row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] in other_pieces:
            moves.append(((row, col), (row - 1, col - 1)))
        if color == "black" and row - 1 >= 0 and col + 1 < 8 and board[row - 1][col + 1] in other_pieces:
            moves.append(((row, col), (row - 1, col + 1)))
        
        return moves
    def _get_knight_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        other_pieces = ['♜', '♞', '♝', '♛', '♚','♟'] if color == "black" else ['♖', '♘', '♗', '♕', '♔', '♙']
        moves = []
        if row - 2 >= 0 and col - 1 >= 0 and (board[row - 2][col - 1] == ' ' or board[row - 2][col - 1] in other_pieces):
            moves.append(((row, col), (row - 2, col - 1)))
        if row - 2 >= 0 and col + 1 < 8 and (board[row - 2][col + 1] == ' ' or board[row - 2][col + 1] in other_pieces):
            moves.append(((row, col), (row - 2, col + 1)))
        if row - 1 >= 0 and col - 2 >= 0 and (board[row - 1][col - 2] == ' ' or board[row - 1][col - 2] in other_pieces):
            moves.append(((row, col), (row - 1, col - 2)))
        if row - 1 >= 0 and col + 2 < 8 and (board[row - 1][col + 2] == ' ' or board[row - 1][col + 2] in other_pieces):
            moves.append(((row, col), (row - 1, col + 2)))
        
        if row + 2 < 8 and col - 1 >= 0 and (board[row + 2][col - 1] == ' ' or board[row + 2][col - 1] in other_pieces):
            moves.append(((row, col), (row + 2, col - 1)))
        if row + 2 < 8 and col + 1 < 8 and (board[row + 2][col + 1] == ' ' or board[row + 2][col + 1] in other_pieces):
            moves.append(((row, col), (row + 2, col + 1)))
        if row + 1 < 8 and col - 2 >= 0 and (board[row + 1][col - 2] == ' ' or board[row + 1][col - 2] in other_pieces):
            moves.append(((row, col), (row + 1, col - 2)))
        if row + 1 < 8 and col + 2 < 8 and (board[row + 1][col + 2] == ' ' or board[row + 1][col + 2] in other_pieces):
            moves.append(((row, col), (row + 1, col + 2)))

        return moves
    def _get_rock_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        other_pieces = ['♜', '♞', '♝', '♛', '♚','♟'] if color == "black" else ['♖', '♘', '♗', '♕', '♔', '♙']
        moves = []
        directions = {"forward": True, "backward": True, "left": True, "right": True}
        for step in range(1,8):
            if row - step >= 0 and directions["backward"] == True:
                if board[row - step][col] == ' ':
                    moves.append(((row, col), (row - step, col)))
                elif board[row - step][col] in other_pieces:
                    moves.append(((row, col), (row - step, col)))
                    directions["backward"] = False
                else:
                    directions["backward"] = False
            if row + step < 8 and directions["forward"] == True:
                if board[row + step][col] == ' ':
                    moves.append(((row, col), (row + step, col)))
                elif board[row + step][col] in other_pieces:
                    moves.append(((row, col), (row + step, col)))
                    directions["forward"] = False
                else:
                    directions["forward"] = False
            if col - step >= 0 and directions["left"] == True:
                if board[row][col - step] == ' ':
                    moves.append(((row, col), (row, col - step)))
                elif board[row][col - step] in other_pieces:
                    moves.append(((row, col), (row, col - step)))
                    directions["left"] = False
                else:
                    directions["left"] = False
            if col + step < 8 and directions["right"] == True:
                if board[row][col + step] == ' ':
                    moves.append(((row, col), (row, col + step)))
                elif board[row][col + step] in other_pieces:
                    moves.append(((row, col), (row, col + step)))
                    directions["right"] = False
                else:
                    directions["right"] = False
        return moves
    def _get_bishop_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        other_pieces = ['♜', '♞', '♝', '♛', '♚','♟'] if color == "black" else ['♖', '♘', '♗', '♕', '♔', '♙']
        moves = []
        directions = {"dia": True, "-dia": True, "gonal": True, "-gonal": True}
        for step in range(1,8):
            if row - step >= 0 and col - step >= 0 and directions["-dia"]:
                if board[row - step][col - step] == ' ':
                    moves.append(((row, col), (row - step, col - step)))
                elif board[row - step][col - step] in other_pieces:
                    moves.append(((row, col), (row - step, col - step)))
                    directions["-dia"] = False
                else:
                    directions["-dia"] = False
            if row + step < 8 and col + step < 8 and directions["dia"]:
                if board[row + step][col + step] == ' ':
                    moves.append(((row, col), (row + step, col + step)))
                elif board[row + step][col + step] in other_pieces:
                    moves.append(((row, col), (row + step, col + step)))
                    directions["dia"] = False
                else:
                    directions["dia"] = False
            if row - step >= 0 and col + step < 8 and directions["-gonal"]:
                if board[row - step][col + step] == ' ':
                    moves.append(((row, col), (row - step , col + step)))
                elif board[row - step][col + step] in other_pieces:
                    moves.append(((row, col), (row - step, col + step)))
                    directions["-gonal"] = False
                else:
                    directions["-gonal"] = False
            if row + step < 8 and col - step >= 0 and directions["gonal"]:
                if board[row + step][col - step] == ' ':
                    moves.append(((row, col), (row + step, col - step)))
                elif board[row + step][col - step] in other_pieces:
                    moves.append(((row, col), (row + step, col - step)))
                    directions["gonal"] = False
                else:
                    directions["gonal"] = False
        return moves
    def _get_queen_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        moves = []
        moves.extend(self._get_bishop_moves(board, row, col, color))
        moves.extend(self._get_rock_moves(board, row, col, color))
        return moves
    def _get_king_moves(self, board, row, col, color = None):
        color = self.color if color == None else color
        other_pieces = ['♜', '♞', '♝', '♛', '♚','♟'] if color == "black" else ['♖', '♘', '♗', '♕', '♔', '♙']
        moves = []
        if row - 1 >= 0:
            if board[row - 1][col] == ' ' or board[row - 1][col] in other_pieces:
                moves.append(((row, col), (row - 1, col)))
            if col - 1 >= 0 and (board[row - 1][col - 1] == ' ' or board[row - 1][col - 1] in other_pieces):
                moves.append(((row, col), (row - 1, col - 1)))
            if col + 1 < 8 and (board[row - 1][col + 1] == ' ' or board[row - 1][col + 1] in other_pieces):
                moves.append(((row, col), (row - 1, col + 1)))
        if row + 1 < 8:
            if board[row + 1][col] == ' ' or board[row + 1][col] in other_pieces:
                moves.append(((row, col), (row + 1, col)))
            if col - 1 >= 0 and (board[row + 1][col - 1] == ' ' or board[row + 1][col - 1] in other_pieces):
                moves.append(((row, col), (row + 1, col - 1)))
            if col + 1 < 8 and (board[row + 1][col + 1] == ' ' or board[row + 1][col + 1] in other_pieces):
                moves.append(((row, col), (row + 1, col + 1)))
        if col - 1 >= 0 and (board[row][col - 1] == ' ' or board[row][col - 1] in other_pieces):
            moves.append(((row, col), (row, col - 1)))
        if col + 1 < 8 and (board[row][col + 1] == ' ' or board[row][col + 1] in other_pieces):
            moves.append(((row, col), (row, col + 1)))


        if self.left_castling:
            if board[row][col - 1] == ' ' and board[row][col - 2] == ' ' and board[row][col - 3] == ' ':
                moves.append(((row, col), (row, col - 2), (row, 0), (row, 3)))
        if self.right_castling:
            if board[row][col + 1] == ' ' and board[row][col + 2] == ' ':
                moves.append(((row, col), (row, col + 2), (row, 7), (row, 5)))
        return moves