# Wordle-like game(? - I don't know how Wordle works): hangman, except you guess the word with other words. Various hints are given based on correct letters (in the correct position or simply in the word)

"""
1. random *Word* picked from dictionary
2. Player will have set number of guesses (lives) to input words of equal length [to the actual *Word*] to get hints.
3. Hints include:
    3a. If your *guess* contains a letter(s) that are also found in the *Word* (regardless of position), highlight them
    3b. If highlighted letters are further highlighted if they are also in the correct position.
4. Implement scoring system based on effeciency of guessing
"""


from english_words import english_words_lower_alpha_set
import random

# set characters to avoid 'non-words'
other_char = ['!','@','#','$','%','^','&','*','(',')']
bad_words = list()

#turn dictionary from set to list
dictionary = list(english_words_lower_alpha_set)
# sort dictionary list in alphabetical order
dictionary.sort()

# search through dictionary, remove words with *other_char*
# loop_count is number of times you want to loop the below code, because (for some reason) it doesn't work once around and needs multiple passes to remove all *bad_words*
loop_count = 2
while loop_count > 0:
    for word in dictionary:
        for char in word:
            if char in other_char:
                dictionary.remove(word)
    loop_count-=1

# print('dictionary#:', dictionary)
#print(dictionary)
#print(random.choice(dictionary))




print('-----------\nEnd Diagnostics\n-----------')

def pick_word():
    global word
    word = random.choice(dictionary)
    global word_length
    word_length = len(word)
    global hidden_word
    hidden_word = list()

def instructions():
    print("1. A random English *Word* has been chosen.\n2. It is", word_length, "letters long.\n3. Guess other words of the same length to get hints about the letters in the *Word*.\n4. Guess the *Word* before you run out of lives.\n- Type '_exit' to Exit.\n- Type '_instructions' or '_help' to replay instructions.\n")

# display current board
def set_board():
    #print("***",word,"***")
    for char in word:
        hidden_word.append("_")
    print("*Word* is",word_length,"letters long.")
    print(hidden_word)
    global lives
    lives = round(word_length/2)+2
    print("You have:",lives,"lives.")
    print("Make your first guess:")

def guess_word():
    global guess_count
    guess_count = 0
    guess = input()
    if guess == "_exit":
        exit_game()
    elif guess == "_instructions" or guess == "_help":
        instructions()
    elif guess == "_restart":
        start_game()
    elif len(guess) != word_length:
        print("Reminder: Guess words of the same length. Try again.")
    elif guess == word:
        print("YOU WIN!")
        play_again()
    else:
        if guess in dictionary:
            guess_count += 1
            global lives
            lives -= 1
            #print("***word:***",word)
            for char in guess:
                if char in word:
                    for i in range(word_length):
                        if char == word[i]:
                            hidden_word[i] = char
            print(hidden_word)
            if lives > 1:
                print("You now have",lives,"lives. Guess again:")
            else:
                print("You now have",lives,"life left. GUess again:")
        else:
            print("Your guess is not a real word. You lose 1 life. Try again.")
            lives -= 1
            if lives > 1:
                print("You have", lives, "left")
            else:
                print("You now have",lives,"life left. GUess again:")


def play_again():
    print("Word was:",word,"\n Do you want to play again? (Y/N)")
    while True:
        play_again = input()
        if play_again in ('Yes','yes','Y','y'):
            start_game()
        elif play_again in ("No",'no','N','n'):
            print("Thanks For Playing!")
            exit_game()
        else:
            print("Try again. Do you want to play again? (Y/N)")


def exit_game():
    exit()

def game_over():
    print("GAME OVER: You have no lives left!\nPlay Again?(Y/N)")
    play_again()

def start_game():
    pick_word()
    instructions()
    set_board()
    while lives > 0:
        guess_word()
    game_over()


start_game()
