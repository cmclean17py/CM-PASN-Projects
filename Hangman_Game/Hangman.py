import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) # randomly choose a word from words.py
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # The set() function creates a set object
    alphabet = set(string.ascii_uppercase) # ascii_uppercase will give the uppercase letters ‘ABCDEFGHIJKLMNOPQRSTUVWXYZ’
    used_letters = set()

    lives = 6

    # greet user
    print('Welcome to Hangman')
    # get user input
    while len(word_letters) > 0 and lives > 0:
        # Letters Used
        print('You have used these letters so far: ', ' '.join(used_letters)) # Join all items into a string, using a space character as separator

        # what current word is so far (i.e W – R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
        elif user_letter in used_letters:
            print('You already chose this character, please choose another')
        else:
            print('Invalid character, please try again ')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print('You died, sorry the word was', word_letters)
    else:
        print('You guessed the word', word, '!!')

hangman()

