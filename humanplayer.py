from nezhaplayer import ChessPlayer
class HumanPlayer(ChessPlayer):
    def __init__(self, color):
        super().__init__(color)
        self.color = color

    def get_move(self, board):
        while True:
            try:
                move_input = input(f"Enter the move you want to do ({self.color}): ")
                if move_input == "exit":
                    raise KeyboardInterrupt
                move = self.parse_move(move_input)
                legal_moves = self.get_legal_moves(board)
                normalized = [move[0:2] for move in self.get_available_moves(board)]
                if move in legal_moves:
                    return move
                elif move in normalized:
                    index = normalized.index(move)
                    return legal_moves[index]
                else:
                    print("Invalid move.")
            except KeyboardInterrupt:
                print("Exiting game.")
                exit()
            except ValueError:
                print("Invalid input format. The correct format is 'initial_row,initial_col final_row,final_col'.")

    def parse_move(self, move_input):
        coords = move_input.split()
        if len(coords) != 2:
            raise ValueError
        initial_coords = tuple(map(int, coords[0].split(',')))
        final_coords = tuple(map(int, coords[1].split(',')))
        return (initial_coords, final_coords)
