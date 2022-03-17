import random

#list of hangman pictures in different stages in sequence of number of guesses left
HANGMAN_PICS = ['''
       +---+
           |
           |
           |
          ===''', '''
       +---+
       O   |
           |
           |
          ===''', '''
       +---+
       O   |
       |   |
           |
          ===''', '''
       +---+
       O   |
      /|   |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
           |
          ===''', '''
       +---+
       O   |
      /|\  |
      /    |
          ===''', '''
       +---+
       O   |
      /|\  |
      / \  |
          ===''']

#list of words from which one word will be selected at random for user to guess
words= [
"Aardvark"
"Alligator",
"Alpaca",
"Anaconda",
"Ant",
"Antelope",
"Bat",
"Bee",
"Bird",
"Blue Whale",
"Buffalo",
"Butterfly",
"Camel",
"Cat",
"Caterpillar",
"Cheetah",
"Chicken",
"Chimpanzee",
"Chipmunk",
"Cobra",
"Cow",
"Crab",
"Crocodile",
"Crow",
"Cuckoo",
"Deer",
"Dinosaur",
"Dog",
"Dolphin",
"Donkey",
"Dove",
"Duck",
"Eagle",
"Elephant",
"Fish",
"Flamingo",
"Fly",
"Fox",
"Frog",
"Goat",
"Goose",
"Gorilla",
"Hamster"
,"Hare",
"Hawk",
"Hippopotamus",
"Horse",
"Hummingbird",
"Husky",
"Iguana",
"Impala",
"Kangaroo",
"Lemur",
"Leopard",
"Lion",
"Llama",
"Lobster",
"lizard",
"Monkey",
"Mosquito",
"Moth",
"Mouse",
"Octopus",
"Ostrich",
"Owl",
"Ox",
"Oyster",
"Panda",
"Parrot",
"Peacock",
"Penguin",
"Pig",
"Pigeon",
"Polar bear",
"Rabbit",
"Raccoon",
"Rat",
"Rooster",
"Seal",
"Sheep",
"Sloth",
"Snail",
"Snake",
"Spider",
"Tiger",
"Whale",
'Wolf',
'Zebra'
]

#function to select a random word from list of words
def getRandomWord():
    word= random.choice(words)
    return word

#function to display details like missing words ,correctly guessed words etc
def displayBoard(missedLetters, correctLetters, secretWord):
    
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    #to check the number of blank spaces left
    blanks = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            #it will insert the ith letter of secretWord at ith position in blanks variable
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        #vowels aren't hidden 
        if secretWord[i] in 'aeiou':
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    #display guessed letters in their right position
    for letter in blanks:
        print(letter, end=' ')
    print()

#this function checks various conditions while user takes a guess
def getGuess(alreadyGuessed):
    while True:
        #asks for an input and converts in lowercase for easier comparison
        guess= input('Guess a letter: ').lower()
        
        if len(guess) !=1:
            print('Kindly enter a single letter only!')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER from english alphabet.')
        else:
            return guess

#function to check if user wants to play again
def playAgain():
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

print('H A N G M A N')
#initialising
missedLetters = ''
correctLetters= ''
#stores a random word from list to be guessed by user
secretWord = getRandomWord()
#converts secretWord to lowercase
secretWord=secretWord.lower()
#stores vowels (if any) in secretWord 
correctLetters1 = [each for each in secretWord if each in 'aeiou']
#converts list into string for comparision
correctLetters= correctLetters.join(correctLetters1)
gameOver = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #stores the guess from user
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord :
        correctLetters = correctLetters + guess  

        #assuming the secretWord is guessed
        foundAllLetters = True
        #cross-checking the assumption
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord +
                   '"! You have won!')
            gameOver = True
        
    else:
        missedLetters = missedLetters + guess
        
        #if user runs out of chance to guess the word
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +str(len(missedLetters)) + ' missed guesses and ' +str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameOver = True

    #checking if user wants to play again or stop
    if gameOver:
        if playAgain():
            missedLetters = ''
            correctLetters= ''
            secretWord = getRandomWord()
            secretWord=secretWord.lower()
            correctLetters1 = [each for each in secretWord if each in 'aeiou']
            correctLetters= correctLetters.join(correctLetters1)
            gameOver = False
        else:
            break
