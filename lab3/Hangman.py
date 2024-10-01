'''
Hangman.py
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)

        ### Your code goes here:###
            # use a map to keep track of the guessed letters, correct letters, and incorrect letters
            # at most 10 different letters in the word
            # only allow alphabetic characters
            # only allow one character at a time
            # convert to lowercase 
            # correctly identify if letter appears in word more than once
            # 10 guesses total including correct and incorrect guesses
            # if success print "congratulations" 
            # if failure print "Sorry, dude, the word is: " + word
        print('Welcome to Hangman!')
        print('Guess the word')
        print('You have 10 guesses')
        print('Good Luck!')
        print(word)
        guesses = 0
         # check if the guess is a letter A-Z and only one character
        while guesses < 10:
           # print(word)
            ch = input('Enter a guess:').lower()
            if not ch.isalpha():
                print('Character is not a letter. Please enter a letter.')
            elif len(ch) != 1:
                print('Please enter only one letter.')
            elif ch in self.wordguess:
                print('Letter already guessed.')
            else:
                guesses += 1
                if guesses == 10:
                    print('Sorry, dude, the word is: ' + word)
                    break
                print('Guesses Remaining: ' + str(10 - guesses))
                bool_list = list(map(lambda actual: True if ch == actual else False, word))
                for i in range(len(self.wordguess)):
                    if bool_list[i] == True:
                        self.wordguess[i] = ch
            if self.wordguess == list(word):
                print('Congratulations')
                break
            
            
            
        # check if the character is in the word
        # list of booleans in a list that says whether the character is in each index of the word
       # bool_list = lambda ch, actual: True if ch is actual else False
        
       
        
        
        
           
            


if __name__ == "__main__":

    game = Hangman()

    game.playgame()
