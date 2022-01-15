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

print('dictionary#:', dictionary)

print('-----------\nEnd Diagnostics\n-----------')

# start the game: reset game, choose a new *word*
def start_game():
    print('New Game')
    #randomly select a *Word*
    word = dictionary[random.randrange(0,len(dictionary))]
    print('Random Word Is:',word,'(should be censored)')
    word_length = len(word)
    #print(word_length)
    hidden_word = list()
    for i in range(word_length):
        hidden_word.append('_')
    print(hidden_word)
    global lives # does this need to be global?
    lives = (word_length/2)+2

def make_guess():
    good_guess = 0
    while good_guess == 0:
        print('Guess the word:')
        guess = input()
        if len(guess) is len(word):
            good_guess +=1
        else:
            print('Guess the word:')

start_game()
while lives > 0:
    make_guess()
    if good_guess > 0:
        continue
