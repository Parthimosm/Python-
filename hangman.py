import random, time, collections
HANGMANPICS = ["""
-----
|   |
|   
|
|
| 
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\ 
|   | 
|   | 
|  | | 
|  
|
--------
"""]

bankOfSecretWords = ["elephant","organic","investment","canadian","birthday","hunter","helicopter","potato","hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"] 

def getRandomWord(wordList):
   # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]
    bankOfSecretWords.remove(wordIndex)

def displayBoard(HANGMANPICS, incorrectLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(incorrectLetters)])
    print()
    print('Missed letters:', end=' ')
    for letter in incorrectLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks: # show the secret word with spaces in between each letter
         print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

#Asking user if they want to play
print ("Welcome to my Game of Hangman")
print("\n")
userPlaying = str(input("Do you want to play Hangman?:"))
if "yes" in userPlaying or "sure" in userPlaying:
	#Asking user name
	userName = str(input("What is your name?:"))
	print("Have fun playing HANGMAN",userName)
else:
	print("Well you are missing out")
	quit()

print('H A N G M A N')
incorrectLetters = ''
correctLetters = ''
secretWord = getRandomWord(bankOfSecretWords)
gameIsDone = False
wins = 0
loses = 0
hintPos = random.randint(0, len(secretWord)) 

while True:
    displayBoard(HANGMANPICS, incorrectLetters, correctLetters, secretWord)
     # Let the player type in a letter.
    guess = getGuess(incorrectLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess
        # Check if the player has won
        foundAllLetters = True
        for pos in range(len(secretWord)):
            if secretWord[pos] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            wins = wins + 1
            gameIsDone = True
    else:
        incorrectLetters = incorrectLetters + guess
         # Check if player has guessed too many times and lost
        if len(incorrectLetters) == len(HANGMANPICS) - 1:
            displayBoard(HANGMANPICS, incorrectLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(incorrectLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            loses = loses + 1
            gameIsDone = True
        if len(incorrectLetters) == 6:
            hint = input("do you want a hint?(yes, no)")
            if "yes" in hint:
                if secretWord[hintPos] not in correctLetters: 
                    correctLetters = correctLetters + secretWord[hintPos]
                    displayBoard(HANGMANPICS, incorrectLetters, correctLetters, secretWord)

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        print("wins:", wins)
        print("loses:", loses)
        replay = input("Do you want to play again(yes, no)")
        if replay == "yes":
            incorrectLetters = ''
            correctLetters = ''
            secretWord = getRandomWord(bankOfSecretWords)
            gameIsDone = False
        else:
            time.sleep(5) 
            quit()


