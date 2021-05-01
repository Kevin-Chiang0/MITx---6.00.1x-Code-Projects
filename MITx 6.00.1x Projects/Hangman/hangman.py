# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for x in secretWord:
      if x in lettersGuessed:
        pass
      else:
        return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordPrint = ''
    for x in secretWord:
      if x in lettersGuessed:
        wordPrint += x
      else:
        wordPrint += " _ "
    print(wordPrint)


def getAvailableLetters(lettersGuessed, abc):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    for x in lettersGuessed:
      if abc.find(x) > -1:
        abc = abc.replace(x,"")
      else:
        pass
    print("\n" + abc, "letters are left to guess!\n")
    return abc
    # FILL IN YOUR CODE HERE...
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    counter = 0
    lettersGuessed = []
    abc = "abcdefghijklmnopqrstuvwxyz"
    print("Welcome to Hangman! \n")
    print("The secret word has", len(secretWord), "letters\n" )
    
    while isWordGuessed(secretWord, lettersGuessed) is False:
      counter += 1
      print("\nThis is round number", counter, "\n")
      guess = input("What letter would you like to guess this round? \n")
      if abc.find(guess) == -1 or len(guess) > 1:
        print("\nEither that wasn't a letter or you already guessed that.\n")
        counter -= 1
        getGuessedWord(secretWord, lettersGuessed)
        getAvailableLetters(secretWord, abc)
      else:
        lettersGuessed.append(guess)
        getGuessedWord(secretWord, lettersGuessed)
        abc = getAvailableLetters(lettersGuessed, abc)
    print("Congrats! the word was", secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)