import random


word_list = [
    'wares',
    'soup',
    'mount',
    'extend',
    'brown',
    'expert',
    'tired',
    'humidity',
    'backpack',
    'crust',
    'dent',
    'market',
    'knock',
    'smite',
    'windy',
    'coin',
    'throw',
    'silence',
    'bluff',
    'strict',
    'mystic',
    'film',
    'guide',
    'strain',
    'bishop',
    'settle',
    'plateau',
    'emigrate',
    'marching',
    'optimal',
    'medley',
    'endanger'
]


def get_word():
    """This function chooses a word at random from the words.py file using 
    the random module imported"""
    word = random.choice(word_list)
    return word.upper()


def start(word):
    """ This functions starts the game and iterates through 
    the responses using a while loop depending on the input 
    the player enters
    """
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("I ask you to guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You silly goose, you already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word you fool.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Oh look, you got lucky,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Ppfftt! You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word you dolt.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Seriosuly? Are you ill? That is incorrect!.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Huzzah, you are correct! You win! This soul has been spared")
    else:
        print("Out of tries. The word was " + word + ". Maybe next time!")


def display_hangman(tries):
    """ This function contains the stages and the depictions of the 
    hanged mans noose"""
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    start(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        start(word)


if __name__ == "__main__":
    main()