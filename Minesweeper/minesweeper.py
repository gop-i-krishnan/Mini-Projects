import random


def main():
    class Board:
        def __init__(self, dim_size, num_bombs):
            self.dim_size = dim_size
            self.num_bombs = num_bombs
            self.board = self.make_new_board()
            self.assign_values_to_board()
            self.dug = set()  # Keep track of dug locations

        def make_new_board(self):
            # Create a new board with `dim_size x dim_size` dimensions
            board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            bombs_planted = 0

            while bombs_planted < self.num_bombs:
                loc = random.randint(0, self.dim_size**2 - 1)
                row = loc // self.dim_size
                col = loc % self.dim_size

                if board[row][col] == "*":
                    continue  # Skip if a bomb is already planted

                board[row][col] = "*"  # Plant a bomb
                bombs_planted += 1

            return board

        def assign_values_to_board(self):
            # Assign a number (0-8) to each cell, representing the number of neighboring bombs
            for r in range(self.dim_size):
                for c in range(self.dim_size):
                    if self.board[r][c] == "*":
                        continue
                    self.board[r][c] = self.get_num_neighbouring_bombs(r, c)

        def get_num_neighbouring_bombs(self, row, col):
            # Calculate the number of bombs in adjacent cells
            num_neighbouring_bombs = 0
            for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
                for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                    if r == row and c == col:
                        continue  # Skip the current cell
                    if self.board[r][c] == "*":
                        num_neighbouring_bombs += 1

            return num_neighbouring_bombs

        def dig(self, row, col):
            # Dig at the specified location
            self.dug.add((row, col))  # Mark the cell as dug

            if self.board[row][col] == "*":
                return False  # Hit a bomb, game over!
            elif self.board[row][col] > 0:
                return True  # Dug a cell with a neighboring bomb count

            # If no neighboring bombs, recursively dig adjacent cells
            for r in range(max(0, row - 1), min(self.dim_size, row + 2)):
                for c in range(max(0, col - 1), min(self.dim_size, col + 2)):
                    if (r, c) in self.dug:
                        continue  # Skip already dug cells
                    self.dig(r, c)

            return True

        def __str__(self):
            # Create a string representation of the board for display
            visible_board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)]
            for r in range(self.dim_size):
                for c in range(self.dim_size):
                    if (r, c) in self.dug:
                        visible_board[r][c] = str(self.board[r][c])
                    else:
                        visible_board[r][c] = " "
            return "\n".join([" | ".join(row) for row in visible_board])

    def play(dim_size=10, num_bombs=10):
        # Start the game
        board = Board(dim_size, num_bombs)
        safe = True  # Track if the game is still safe

        while len(board.dug) < dim_size**2 - num_bombs:
            print(board)
            user_input = input("Where would you like to dig? Input as row,col: ")
            row, col = map(int, user_input.split(","))

            if row < 0 or row >= dim_size or col < 0 or col >= dim_size:
                print("Invalid location. Try again.")
                continue

            safe = board.dig(row, col)
            if not safe:
                break  # Hit a bomb, game over

        if safe:
            print("Congratulations! You win!")
        else:
            print("Game Over!")
            # Reveal the entire board
            board.dug = {(r, c) for r in range(dim_size) for c in range(dim_size)}
            print(board)

    # Start the game
    play()


if __name__ == "__main__":
    main()
