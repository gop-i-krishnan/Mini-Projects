import random

def play():
    print("Press 'R' for rock\nPress 'S' for scissors\nPress 'P' for paper")
    score = 0  # Initialize score variable
    while True:
        user = input("Enter your choice: ").upper()  
        computer = random.choice(["R", "S", "P"])
        
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == "R" and computer == "S") or (user == "S" and computer == "P") or (user == "P" and computer == "R"):
            print("You win! 🎉")
            score += 1  # Increment score on win
            print(f"Your current score: {score}")
        elif user in ["R", "S", "P"]:
            print("You lose! 😢\nPress Enter to play again")
        else:
            print("Invalid choice. Please select R, S, or P.")
            continue

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print(f"Your final score: {score}")
            break

def main():
    print("***************************************")
    print("Welcome to Rock, Paper, and Scissors Game 🎊")
    print("***************************************\n")
    is_running = True
    while is_running:
        choice = input("1. Play\n2. Exit\nEnter your choice: ").lower()
        if choice == "1" or choice == "play":
            play()
        elif choice == "2" or choice == "exit":
            print("Thank you for playing!\nPress Enter to exit the game.")
            input()
            is_running = False
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
