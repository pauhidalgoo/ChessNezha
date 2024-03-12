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
            return legal_moves[0]
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
        return moves
    def _get_pawn_moves(self, board, row, col):
        moves = []
        if self.color == "black" and row - 1 >= 0 and board[row - 1][col] == ' ':
            moves.append(((row, col), (row - 1, col)))
        if self.color == "white" and row + 1 < 8 and board[row + 1][col] == ' ':
            moves.append(((row, col), (row + 1, col)))
        return moves
    def _get_knight_moves(self, board, row, col):
        pass
    def _get_rock_moves(self, board, row, col):
        pass
    def _get_bishop_moves(self, board, row, col):
        pass
    def _get_queen_moves(self, board, row, col):
        pass
    def _get_king_moves(self, board, row, col):
        pass