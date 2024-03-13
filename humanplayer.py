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
                if move in self.get_legal_moves(board):
                    return move
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
