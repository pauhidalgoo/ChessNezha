import random
class ChessPlayer:
    def __init__(self, color):
        self.color = color
        if self.color== "white":
            self.pieces =  ['♜', '♞', '♝', '♛', '♚','♟']
        elif self.color=="black":
            self.pieces = ['♖', '♘', '♗', '♕', '♔', '♙']
        else:
            print("The color is incorrect. It must be white or black")
            raise
        pass
    def get_move(self, board):
        legal_moves = self.get_legal_moves(board)
        if legal_moves:
            return legal_moves[random.randint(0, len(legal_moves)-1)]
        else:
            return None
    def get_legal_moves(self, board):
        legal_moves = []
        for row_id, row in enumerate(board):
            for col_id, piece in enumerate(row):
                if piece in self.pieces:
                    moves = self.get_piece_moves(board, row_id, col_id)
                    legal_moves.extend(moves)
        return legal_moves
    def get_piece_moves(self, board, row, col):
        piece = board[row][col]
        moves = []
        if piece == '♙' or piece == '♟':
            moves.extend(self._get_pawn_moves(board, row, col))
        if piece == '♖' or piece == '♜':
            moves.extend(self._get_rock_moves(board, row, col))
        if piece == '♗' or piece == '♝':
            moves.extend(self._get_bishop_moves(board, row, col))
        if piece == '♕' or piece == '♛':
            moves.extend(self._get_queen_moves(board, row, col))
        if piece == '♔' or piece == '♚':
            moves.extend(self._get_king_moves(board, row, col))
        if piece == '♘' or piece == '♞':
            moves.extend(self._get_knight_moves(board, row, col))
        return moves
    def _get_pawn_moves(self, board, row, col):
        moves = []
        if self.color == "black" and row - 1 >= 0 and board[row - 1][col] == ' ':
            moves.append(((row, col), (row - 1, col)))
        if self.color == "white" and row + 1 < 8 and board[row + 1][col] == ' ':
            moves.append(((row, col), (row + 1, col)))
        if self.color == "black" and row == 6 and board[row - 2][col] == ' ':
            moves.append(((row, col), (row - 2, col)))
        if self.color == "white" and row == 1 and board[row + 2][col] == ' ':
            moves.append(((row, col), (row + 2, col)))
        return moves
    def _get_knight_moves(self, board, row, col):
        moves = []
        if row - 2 >= 0 and col - 1 >= 0 and board[row - 2][col - 1] == ' ':
            moves.append(((row, col), (row - 2, col - 1)))
        if row - 2 >= 0 and col + 1 < 8 and board[row - 2][col + 1] == ' ':
            moves.append(((row, col), (row - 2, col + 1)))
        if row - 1 >= 0 and col - 2 >= 0 and board[row - 1][col - 2] == ' ':
            moves.append(((row, col), (row - 1, col - 2)))
        if row - 1 >= 0 and col + 2 < 8 and board[row - 1][col + 2] == ' ':
            moves.append(((row, col), (row - 1, col + 2)))
        
        if row + 2 < 8 and col - 1 >= 0 and board[row + 2][col - 1] == ' ':
            moves.append(((row, col), (row + 2, col - 1)))
        if row + 2 < 8 and col + 1 < 8 and board[row + 2][col + 1] == ' ':
            moves.append(((row, col), (row + 2, col + 1)))
        if row + 1 < 8 and col - 2 >= 0 and board[row + 1][col - 2] == ' ':
            moves.append(((row, col), (row + 1, col - 2)))
        if row + 1 < 8 and col + 2 < 8 and board[row + 1][col + 2] == ' ':
            moves.append(((row, col), (row + 1, col + 2)))

        return moves
    def _get_rock_moves(self, board, row, col):
        moves = []
        directions = {"forward": True, "backward": True, "left": True, "right": True}
        for step in range(1,8):
            if row - step >= 0 and directions["backward"] == True:
                if board[row - step][col] == ' ':
                    moves.append(((row, col), (row - step, col)))
                else:
                    directions["backward"] = False
            if row + step < 8 and directions["forward"] == True:
                if board[row + step][col] == ' ':
                    moves.append(((row, col), (row + step, col)))
                else:
                    directions["forward"] = False
            if col - step >= 0 and directions["left"] == True:
                if board[row][col - step] == ' ':
                    moves.append(((row, col), (row, col - step)))
                else:
                    directions["left"] = False
            if col + step < 8 and directions["right"] == True:
                if board[row][col + step] == ' ':
                    moves.append(((row, col), (row, col + step)))
                else:
                    directions["right"] = False
        return moves
    def _get_bishop_moves(self, board, row, col):
        moves = []
        directions = {"dia": True, "-dia": True, "gonal": True, "-gonal": True}
        for step in range(1,8):
            if row - step >= 0 and col - step >= 0 and directions["-dia"]:
                if board[row - step][col - step] == ' ':
                    moves.append(((row, col), (row - step, col - step)))
                else:
                    directions["-dia"] = False
            if row + step < 8 and col + step < 8 and directions["dia"]:
                if board[row + step][col + step] == ' ':
                    moves.append(((row, col), (row + step, col + step)))
                else:
                    directions["dia"] = False
            if row - step >= 0 and col + step < 8 and directions["-gonal"]:
                if board[row - step][col + step] == ' ':
                    moves.append(((row, col), (row - step , col  + step)))
                else:
                    directions["-gonal"] = False
            if row + step < 8 and col - step >= 0 and directions["gonal"]:
                if board[row + step][col - step] == ' ':
                    moves.append(((row, col), (row + step, col - step)))
                else:
                    directions["gonal"] = False
        return moves
    def _get_queen_moves(self, board, row, col):
        moves = []
        moves.extend(self._get_bishop_moves(board, row, col))
        moves.extend(self._get_rock_moves(board, row, col))
        return moves
    def _get_king_moves(self, board, row, col):
        moves = []
        if row - 1 >= 0 and board[row - 1][col] == ' ':
            moves.append(((row, col), (row - 1, col)))
            if col - 1 >= 0 and board[row][col - 1] == ' ':
                moves.append(((row, col), (row, col - 1)))
                moves.append(((row, col), (row - 1, col - 1)))
            if col + 1 < 8 and board[row][col + 1] == ' ':
                moves.append(((row, col), (row, col + 1)))
                moves.append(((row, col), (row - 1, col + 1)))
        if row + 1 < 8 and board[row + 1][col] == ' ':
            moves.append(((row, col), (row + 1, col)))
            if col - 1 >= 0 and board[row][col - 1] == ' ':
                moves.append(((row, col), (row + 1, col - 1)))
            if col + 1 < 8 and board[row][col + 1] == ' ':
                moves.append(((row, col), (row + 1, col + 1)))
        return moves