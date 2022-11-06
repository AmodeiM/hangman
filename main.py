from hangman_art import logo, stages
from hangman_words import word_list
import random

# Start
print(logo)

# Generate a random word
word = random.choice(word_list)
# For debugging, delete later
print(word)

# Generate as many blanks as letters in the word
blanks = ["_" for letter in word]
print(blanks)

# GameLoop starts here
lives = len(stages)
# Flag to end game loop when game over
game_over = False
# List to keep track of guessed letters
guessed_letters = []
while not game_over:
    # Ask the user to guess a letter
    user_guess = input("Guess a letter: ")
    index = 0
    # Check if user already guessed that letter
    if user_guess not in guessed_letters:
        # add guess to list of guessed letters
        guessed_letters.append(user_guess)
        # Is the guessed letter in the word?
        if user_guess in word:
            for letter in word:
                # Yes:
                if user_guess == letter:
                    # Replace the blanks with the letter
                    blanks[index] = user_guess
                    # Are all the blanks filled?
                    if "_" not in blanks:
                        # no: Game over, user wins
                        print(f"You Win! 🏆 The word was {word}")
                        game_over = True
                index += 1
            # print(blanks)
        # No: lost a life
        else:
            lives -= 1
            # Have the run out of lives?
            if lives == 0:
                print(f"Game Over. You lost. 😢 The word was {word}")
                game_over = True
            print(stages[lives])
        print(blanks)
    else:
        print("You already guessed that letter")
