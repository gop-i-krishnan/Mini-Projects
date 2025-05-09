import random


words = (
    # Fruits
    "apple", "orange", "banana", "grape", "mango", "papaya",
    "pineapple", "watermelon", "strawberry", "blueberry",

    # Animals
    "elephant", "kangaroo", "giraffe", "penguin", "dolphin",
    "crocodile", "cheetah", "octopus", "butterfly", "hedgehog",

    # Countries
    "australia", "germany", "india", "canada", "brazil",
    "france", "japan", "mexico", "norway", "argentina",

    # Objects
    "laptop", "telescope", "backpack", "umbrella", "bicycle",
    "compass", "keyboard", "scissors", "guitar", "notebook",

    # Sports
    "football", "basketball", "cricket", "tennis", "baseball",
    "hockey", "badminton", "swimming", "archery", "gymnastics",

    # Colors
    "red", "blue", "yellow", "green", "purple",
    "orange", "magenta", "violet", "cyan", "indigo",

    # Jobs/Occupations
    "doctor", "engineer", "teacher", "plumber", "pilot",
    "lawyer", "mechanic", "architect", "journalist", "scientist",

    # Science Terms
    "gravity", "molecule", "electron", "planet", "galaxy",
    "spectrum", "atom", "photosynthesis", "energy", "circuit",

    # Mythical Creatures
    "dragon", "phoenix", "unicorn", "mermaid", "griffin",
    "werewolf", "centaur", "hydra", "sphinx", "kraken"
)


hangman_art = {
                0: ("   ",
                    "   ",
                    "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                3: (" o ",
                    "/| ",
                    "   "),
                4: (" o ",
                    "/|\\",
                    "   "),
                5: (" o ",
                    "/|\\",
                    "/  "),
                6: (" o ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print('Guess the word: '+" ".join(hint))

def display_answer(answer):
    print('The answer was',answer)

def main():
    answer=random.choice(words)
    hint=["_"]*len(answer)
    wrong_guesses=0
    guessed_letters=set()
    max_guesses = len(hangman_art) - 1
    is_running=True

    print("Welcome to Hangman!")


    while is_running:

        print('************')
        display_man(wrong_guesses)
        print('************')
        display_hint(hint)


        guess=input('Enter a letter: ').lower()

        if len(guess)!=1 or not guess.isalpha():
            print('Invalid input')
            continue

        if guess in guessed_letters:
            print(f'{guess} is already guessed,Please try a another letter!')
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i, letter in enumerate(answer):
                if letter == guess:
                    hint[i] = guess

        else:
            wrong_guesses+=1

        if '_' not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print('Congrats,YOU WON!')
            is_running=False

        elif wrong_guesses>=max_guesses :
            display_man(wrong_guesses)
            display_answer(answer)
            print('\nYOU LOSE,Better luck next time!\n')
            is_running = False


if __name__ == '__main__':
    main()
