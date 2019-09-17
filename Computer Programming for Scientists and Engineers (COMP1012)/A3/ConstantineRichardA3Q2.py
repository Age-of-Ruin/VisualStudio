# ConstantineRichardA3Q2
#
# COMP 1012 SECTION A01
# INSTRUCTOR Terry Andres
# ASSIGNMENT: A3 Question 2
# AUTHOR Richard Constantine
# VERSION [Date of last change: 2013-Nov-10]
#
# PURPOSE: To create a functioning interactive hangman game.

import time
import urllib
import random

def getWordList() :
    """Formats and records words from internet dictionary"""
    
    url = "http://cs.umanitoba.ca/~comp1012/2of12inf.txt"
    flink = urllib.urlopen(url)
    
    words = []
    count = 0
    
    for eachline in flink :
        
        words.append(eachline) # save each line as a word(as formatted in
                               # as formatted in the online document
        words[count] = words[count].strip()
        
        if words[count].count("%") > 0:
            
            words[count] = words[count].replace("%", "") #formats words from        
                                                          #document
        words[count] = words[count].upper()                   
                                                                     
        count += 1            

    return words
        
def selectWord(minLength, maxLength) :
    """Selects random word from dictionary file"""
    
    words = getWordList()
    
    wordsInRange = []
                  
    for count in range(len(words)): 
    
        if len(words[count]) >= minLength and len(words[count]) <= maxLength :
    
            wordsInRange.append(words[count])
            
        
    randomNumber = int((len(wordsInRange)) * random.random()) # generates a random
                                                              # number between 1 and
    word = wordsInRange[randomNumber]                         # and # of words

    return word

def printBanner(word) :
    """Prints Intro Banner"""
    
    wordLen = len(word)
    
    banner =( """WELCOME TO HANGMAN!\nYOU WILL GUESS A WORD WITH %d LETTERS!
                \nEach time you get the answer wrong, we will add a stroke."""
                %(wordLen) )
                
    print banner	


def showWord(word, guessed) :
    """Determines and shows letters successfully guessed in chosen word"""
    
    blankWord = ""
    blankList = []
    
    for blanks in range (len(word)) :
        
        blankWord += "_ " # creates word filled with blanks
    
    blankList = blankWord.split(" ")
        
    for wordLetter in range (len(word)) :         # check if letter is
                                                   # in guessed letters
        for guessedLetter in range (len(guessed)):
            
            if word[wordLetter] == guessed[guessedLetter]  :
                    
                blankList[wordLetter] = guessed[guessedLetter] 
                    
                blankWord = " ".join(blankList) # format updated word

    return blankWord


def askForInput(word, guessed, pic) :
    
    blankWord = word
    blankWord = showWord(word, guessed) # retrieve word filled with blanks
    
    currPic = pic %(guessed, blankWord) # retrieve and print current picture
    print currPic

    inputUnicode = 0    

    prompt = "What is your next letter (or type your guess)? "
    warning =  " "
    
    userInput = raw_input(prompt).upper()           
    
    while len(warning) > 0 : # checks if input is single letter or guess, if
                              # the letter was already guessed, or if guess
        warning = ""          # is not a letter (outside unicode range)
        
        for letter in range(len(guessed)) :    
                    
            if (len(userInput) != 1 and len(userInput) != len(word) or
                    userInput == guessed[letter]) :
                    
                    warning = ("Invalid Entry: enter a single letter you " 
                               "have not already guessed")
                    
                    userInput = raw_input(warning + "\n\n"  + prompt).upper()         
                
                
            if len(userInput) == 1 :              # correct for unwanted 
                                                  # character input
                inputUnicode = ord(userInput)
                
                if inputUnicode <= 90 and inputUnicode >= 65 :    
            
                    warning = ""
            
                elif inputUnicode <= 122 and inputUnicode >= 97 :
            
                    warning = ""
                    
                else:
                
                    warning = ("Invalid Entry: enter a single letter you " 
                               "have not already guessed")
                    
                    userInput = raw_input(warning + "\n\n"  + prompt).upper()
                
    return userInput
                  
                    
def theEnd() :
    """Ends the program with summary message."""
    
    print "\nProgrammed by Richard Constantine"
    print time.ctime()
    print "End of Processing"
    
    
def main() :
    """Main Script"""
    win = 1 # win boolean (1 resulting in win, 0 resulting in loss)

    CHANGE = [36, 49, 67, 48, 47, 50, 51,  82, 84, 98, 102] # change order of 
                                                           # picture
    wordMin = 6
    wordMax = 8
    word = selectWord(wordMin, wordMax) # select word and print intro banner
    printBanner(word)
    
    userInput = ""
    lettersGuessed = " " # starting values
    lettersLeft = word
    
    changeIndex = 0  # used to iterate picture change indices
    
    picStart = ("  ________  \n |        | \n |          \n |               \n" 
                " |             \n |              \n |              \n |\t\t\t"
                "Letters Guessed: %-26s"  "\t\t WORD: %s") 

    
    picEnd = ("  ________  \n |        | \n |        O \n |      --|--     \n"  
              " |       |     \n |      / \    \n |      /   \      \n |\t\t\t"
              "Letters Guessed: %-26s"  "\t\t WORD: %s")
    
    currPicList = list(picStart)
    
    while len(lettersLeft) > 0 :

        currPic = "".join(currPicList)
            
        userInput = askForInput(word, lettersGuessed, currPic)
        
        userChars = list(set(userInput))
        
        for char in userChars :                         # searches for each
                                                         # unique character
            lettersLeft = lettersLeft.replace(char, "")  # in word (for guesses)
        
        if (lettersGuessed.count(userInput)  == 0 and 
            len(userInput) != len(word)) :          # check that user input
                                                    # is not in letters guessed
            lettersGuessed += userInput             # then concatenates string  
        
        if (changeIndex > 10 and len(lettersLeft) > 0 and userInput != word 
            and word.count(userInput)  == 0) : 
                                                    # once picture is fully 
                                                    #drawn, end the game
            print ("\nSorry, You Lose. Please Try Again \nThe word was %s" 
            % (showWord(word, word)) )
            
            win = 0
            lettersLeft = ""
         
        elif len(userInput) == len(word) and len(lettersLeft) > 0 : # check word
                                                                     # guess
            currPicList[CHANGE[changeIndex]] = picEnd[CHANGE[changeIndex]]
                        
            changeIndex += 1
                    
            print "\nGuess: %s is incorrect" %userInput
            
        elif word.count(userInput) > 1 and len(userInput) != len(word) : 
                                                            
            print ("\nThere are %d %ss"                    #plural correct 
                       % (word.count(userInput),userInput))
                
        elif word.count(userInput) == 1 and len(userInput) != len(word) :
                
            print ("\nThere is %d %s"
                   % (word.count(userInput), userInput))
                
        elif word.count(userInput) == 0 and len(userInput) != len(word) : 
            
            currPicList[CHANGE[changeIndex]] = picEnd[CHANGE[changeIndex]]
                        
            changeIndex += 1
                    
            print "\nThere are no", userInput, "s"
                
    if win == 1 :
        print ("\nCongratulations, You Win!! \nThe word was %s" 
            % (showWord(word, word)) )
    
    
    theEnd()
    
main()