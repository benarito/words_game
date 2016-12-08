import random
import string
import re
import sys

'''
A simple word game
Runs in Python 2.7
Clone the repo and cd words_game
To play in console:
    python words.py
'''

def load_words():
    even_words = []
    odd_words = []
    all_words = []

    # open the file
    text_file = open('words.txt')

    for line in text_file:
        words = line.split()

        for word in words:
            all_words.append(word)
            if len(word)%2 == 0:
                even_words.append(word)
            else:
                odd_words.append(word)
    return odd_words, even_words, all_words

# separate the words into: words with 1. odd number of characters, 2. even number of characters, 3. full list
odd_words, even_words, all_words = load_words()


def check_if_chars_or_word_exists(w):
    '''check if the current characters list exist in the words'''
    if w in all_words:
        return True

    chars_exist = False
    for wd in all_words:
        if w in wd:
            chars_exist = True
            break
    if not chars_exist:
        return True

    return False

def computer_move(w, start_player):
    if len(w) == 0:
        # the computer is starting first
        # choose a random first letter in odd numbered words
        odd_word = random.choice(odd_words)
        random_letter = odd_word[0]
    else:
        '''
        strategy
        - who started? If player started - computer should do an even number  else do an odd number
        - categorize all the words left into odd number words and even number words
        - choose one and add the next character
        - sure way of winning!!
        '''
        len_of_w = len(w)
        try:
            all_probable_words = [i for i in all_words if i[:len_of_w] == w]
            all_odd_words = [i for i in all_probable_words if len(i) %2 != 0]
            all_even_words = [i for i in all_probable_words if len(i) %2 == 0]
        except:
            # no words to pick from
            all_probable_words = []
            all_odd_words = []
            all_even_words = []

        if start_player == 'Computer':
            # do odd words
            if all_odd_words:
                # pick a random word and append its letter
                while True:
                    random_word = random.choice(all_odd_words)
                    print random_word
                    if (len(random_word) != len_of_w + 1) and (random_word[:len_of_w+1] not in all_words):
                        break
                random_letter = random_word[len(w)]
            else:
                # pick from other probable words that are not odd
                random_word = random.choice(all_probable_words)
                random_letter = random_word[len(w)]
        else:
            # even numbers
            if all_even_words:
                # pick a random word and append its letter
                while True:
                    random_word = random.choice(all_even_words)
                    print random_word
                    if (len(random_word) != len_of_w + 1) and (random_word[:len_of_w+1] not in all_words):
                        break
                random_letter = random_word[len(w)]
            else:
                # pick from other probable words that are not odd
                random_word = random.choice(all_probable_words)
                random_letter = random_word[len(w)]

    w += random_letter
    print 'Computer addded letter - {}\n'.format(random_letter)
    return w

def player_move(w):
    # some validations
    while True:
        player_letter = raw_input('Enter a letter: ')
        if re.match("^[a-z]*$", player_letter) and len(player_letter) == 1:
            break
        else:
            print "Only letters are allowed and one character at a time! Please try again!"
    w += player_letter
    return w


def play(start_player, num_rounds):
    print 'You start playing ..\n' if start_player == 'Player' else  'The Computer starts playing .. \n'

    count = 1
    while count < num_rounds+1:
        print 'Playing Round - {}\n'.format(count)

        w =  ''
        lost = False
        while w not in all_words and not lost:
            if start_player == 'Player':
                w=player_move(w)
                lost = check_if_chars_or_word_exists(w)
                if not lost:
                    w=computer_move(w, start_player)
                    lost = check_if_chars_or_word_exists(w)
                    if lost:
                        print 'The Computer lost!!'
                else:
                    print 'You lost!!'
                print 'The current letter(s) are - {}\n'.format(w)
            else:
                w=computer_move(w, start_player)
                lost = check_if_chars_or_word_exists(w)
                print 'The current letter(s) are - {}\n'.format(w)
                if not lost:
                    w=player_move(w)
                    lost = check_if_chars_or_word_exists(w)
                    if lost:
                        print 'You lost!!'
                else:
                    print 'The computer lost!!'
        count += 1


def start():
    print 'Welcome to words game'
    print 'This is a two-player word game, in which the players take turns saying a letter.\nYou play against the computer. If a player says a letter that ends a word, that player loses.\nSimilarly, if a player says a letter from which no word can be spelled, that player loses.\n'
    num_rounds = int(raw_input('How many rounds do you want to play: '))
    print 'The game starts now..\n'

    # choose who to start randomly
    start_player = random.choice(['Computer', 'Player'])
    play(start_player, num_rounds)


if __name__ == '__main__':
    start()

