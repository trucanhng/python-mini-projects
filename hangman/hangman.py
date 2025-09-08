import random
from hangman_words import word_list
from hangman_pics import HANGMAN_PICS


def replace_char(word, pos, char):
    return(word[:pos] + char + word[pos+1:])

def print_current_state(guessed_word, lives):
    print(guessed_word)
    print(HANGMAN_PICS[6 - lives])
    print(f"You have {lives}/6 lives left")
    print("\n" + "="*30 + "\n")
    


if __name__ == "__main__":
    print("Welcome to The Hangman World.")
    
    while True:
        lives = 6
        game_over = False
        category = input("Pick a category (animals/fruits/countries/sports/technology): ").lower()
        while category not in list(word_list.keys()):
            category = input("Invalid category. Pick a category (animals/fruits/countries/sports/technology): ").lower()
        # Pick a random word in the selected category
        word_to_guess = random.choice(word_list[category])
        word_length = len(word_to_guess)
        
        guessed_word = ""
        for _ in word_to_guess:
            guessed_word += "_"
        print(f"The word has {word_length} letters.")

        print_current_state(guessed_word, lives)
        guessed_letter_list = []

        while not game_over:
            guessed_letter = input("Guess a letter: ").lower()
            if not guessed_letter.isalpha() or len(guessed_letter) != 1:
                print("Please enter a single letter.")
                continue
            
            # Track already guessed letters
            if guessed_letter in guessed_letter_list:
                print("You already guessed that letter.")
                continue
            guessed_letter_list.append(guessed_letter)

            # Deterimine if the guessed letter is in word_to_guess
            if guessed_letter in word_to_guess:
                  for index, char in enumerate(word_to_guess):
                      if char == guessed_letter:
                          guessed_word = replace_char(guessed_word, index, char)
            else:
                lives -= 1

            print_current_state(guessed_word, lives)

            # Determine if game is over
            if lives == 0:
                print("Sorry. You lost!")
                print("The correct word was " + word_to_guess)
                game_over = True
            if guessed_word == word_to_guess:
                print("Congratulations. You got it!")
                game_over = True

        if game_over:
            new_game = input("Do you want to start a new game (y/n)? ").lower()
            if new_game == 'n':
                break
                


