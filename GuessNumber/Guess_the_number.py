import random
import time

def guess(x):
    time.sleep(1)
    random_number = random.randint(1, x)
    guess = 0
    score = 0
    is_running = True
    while guess != random_number:
        try:
            guess = int(input(f"Enter a number between 1 and {x}: "))
            score += 1
            if guess == random_number:
                print(f"Yay!\nCongrats, you guessed the right number {random_number}! 😘")
                print(f"Your total tries: {score} times!")
                is_running = False
            elif guess < random_number:
                print(f"Sorry, guess again.\n{guess} is too low!!! 🥲")
            elif guess > random_number:
                print(f"Sorry, guess again.\n{guess} is too high!!! 🥲")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    

def computer_guess(x):
    time.sleep(1)
    low = 1
    high = x
    feedback = ""
    tries = 0

    print(f"Think of a number between 1 and {x}. Let me guess it!")
    time.sleep(2)

    while feedback != "c":
        tries += 1
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # Only one possible number

        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
        elif feedback == "c":
            print(f"Yay! I guessed your number {guess} correctly in {tries} tries! 🎉")
        else:
            print("Please enter valid feedback: H (high), L (low), or C (correct).")

def main():
    is_running=True
    
    print("********************************")
    print("Welcome to Number Guessing Game 🎊")
    print("********************************\n")
    while is_running:
        print("PLAY MODE:\n1. Computer\n2. Manual\n")
        choice = input("Enter your choice: ").lower()
        
        if choice == "2" or choice == "manual":
            print("Choose the level:\n1. Easy\n2. Medium\n3. Hard\n")
            choice = input("Enter your choice: ").lower()

            if choice == "1" or choice == "easy":
                guess(10)
            elif choice == "2" or choice == "medium":
                guess(50)
            elif choice == "3" or choice == "hard":
                guess(100)
            else:
                print("Please enter the correct level.")
        elif choice == "1" or choice == "computer":
            print("Choose the level:\n1. Easy\n2. Medium\n3. Hard\n")
            choice = input("Enter your choice: ").lower()

            if choice == "1" or choice == "easy":
                computer_guess(10)
            elif choice == "2" or choice == "medium":
                computer_guess(50)
            elif choice == "3" or choice == "hard":
                computer_guess(100)
            else:
                print("Please enter the correct level.")
        else:
            print("Please enter the correct mode of play!")

        reply=input("Do you want to play again?(yes/no): ").lower()
        if reply != "yes":
            print("Thank you for playing!\nPress Enter to exit")
            input()
            is_running=False

if __name__ == "__main__":
    main()
