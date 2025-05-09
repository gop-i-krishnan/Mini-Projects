import random
import time

board = [" "] * 10
computer = "X"
human = "O"

def display_board(board):
    print("*" * 10)
    print(f"{board[1]} | {board[2]} | {board[3]}")
    print(f"{board[4]} | {board[5]} | {board[6]}")
    print(f"{board[7]} | {board[8]} | {board[9]}\n")
    print("*" * 10)

def check_win():
    win_conditions = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # Rows
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # Columns
        (1, 5, 9), (3, 5, 7)              # Diagonals
    ]
    for x, y, z in win_conditions:
        if board[x] == board[y] == board[z] and board[x] != " ":
            return True
    return False

def check_draw():
    return board.count(" ") < 2

def is_available(pos):
    return board[pos] == " "

def insert(letter, pos):
    if is_available(pos):
        board[pos] = letter
        display_board(board)
        if check_win():
            print(f"{'Computer' if letter == computer else 'You'} Win!")
            end_game()
        if check_draw():
            print("It's a tie!")
            end_game()
    else:
        print(f"Position {pos} is not available. Try again.")

def computer_move():
    print("Computer's turn...")
    time.sleep(1)
    while True:
        pos = random.randint(1, 9)
        if is_available(pos):
            insert(computer, pos)
            break

def human_move():
    while True:
        try:
            pos = int(input("Enter your position (1-9): "))
            if 1 <= pos <= 9:
                if is_available(pos):
                    insert(human, pos)
                    break
                else:
                    print("Position not available. Try again.")
            else:
                print("Invalid position. Enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def end_game():
    print("Thank you for playing!")
    exit()

# Main game loop
print("Welcome to Tic Tac Toe!")
display_board(board)

while True:
    computer_move()
    human_move()
