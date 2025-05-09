import random
from words import words
import string
from hangman_visual import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()

def hangman(lives):
    word = get_valid_word(words)  # Example: "HELLO"
    word_letters = set(word)  # Letters in the word - {"H", "E", "L", "L", "O"}
    alphabet = set(string.ascii_uppercase)  # All uppercase letters
    used_letters = set()  # Letters guessed by the user

    print("The word has", len(word), "letters.")

    while len(word_letters) > 0 and lives > 0:
        print(lives_visual_dict[lives])  # Display current hangman state

        # Show current progress and used letters
        print(f"\nYou have {lives} lives left. Used letters: {', '.join(used_letters)}")

        # Show the current word with guessed letters
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()

        # Check if the letter is valid and hasn't been guessed yet
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Good job! '{user_letter}' is in the word.")
            else:
                lives -= 1
                print(f"'{user_letter}' is not in the word. You lose a life.")
        elif user_letter in used_letters:
            print(f"You already guessed '{user_letter}'. Try again.")
        else:
            print("Invalid input. Please enter a valid letter.")

    # Game over
    if lives == 0:
        print("\nYou lost! The word was:", word)
        print(lives_visual_dict[0])  # Full hangman at 0 lives
    else:
        print("\nCongratulations! You guessed the word:", word)

def main():
    """Starts the program."""
    print("**********************************")
    print("   Welcome to Hangman Game 🎊  ")
    print("**********************************\n")
    is_running = True
    while is_running:
        choice = input("1. Play\n2. Exit\nEnter your choice: ").lower()
        if choice == "1" or choice == "play":
            print("Choose the level:\n1. Easy\n2. Medium\n3. Hard\n")
            choice = input("Enter your choice: ").lower()

            if choice == "1" or choice == "easy":
                hangman(7)  # Easy level - 7 lives
            elif choice == "2" or choice == "medium":
                hangman(5)  # Medium level - 5 lives
            elif choice == "3" or choice == "hard":
                hangman(3)  # Hard level - 3 lives
            else:
                print("Please enter the correct level.")
            
        elif choice == "2" or choice == "exit":
            print("Thank you for playing!\nPress Enter to exit the game.")
            input()
            is_running = False
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
