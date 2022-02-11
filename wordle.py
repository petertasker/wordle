import random

def receiveFile():
    
    with open("words.txt") as file:
        return file.readlines()

def getGuess(message):
    
    while True:
        
        guess = input(message)
        guess = guess.lower()
        validLength = validLen(guess)
        validWord = validWords(guess)
        if validLength == True and validWord == True:
            break
    return guess

def validLen(guess):
    
    valid = False
    if len(guess) != 5:
        print("Word must be 5 letters")
    else:
        valid = True
    return valid

def validWords(guess):
    
    valid = False
    lines = receiveFile()
    for line in lines:
        line = line.strip()
        if line == guess:
            valid = True
    if valid == False:
        print("Not a valid word")
    return valid
        
def correctAnswer():
   
    lines = receiveFile()
    answer = random.choice(lines)
    answer = answer.strip()
    
    return answer

def workOutPlaces(guess, answer, correctLetters, incorrectLetters, correctPlaces):
    
    count = 0
    for char in guess:
        if char in answer:
            if char not in correctLetters:
                correctLetters += char + ", "
            if char == answer[count]:
                correctPlaces[count] = char
        else:
            if char not in incorrectLetters:
                incorrectLetters += char+", "
        count += 1  
    return correctPlaces, correctLetters, incorrectLetters

def gameEnd(message):
    
    print(message)
    while True:
        
        playing = input("Play again? (Yes/No)")
        if playing.lower() in ("yes", "no"):
            if playing.lower() == "yes":
                playing = True
            else:
                playing = False
            break
    return playing

def welcome():
    
    print("Welcome to wordle!")
    while True:
        
        tutorial = input("Would you like to know how to play? (Yes/No)")
        if tutorial.lower() in ("yes", "no"):
            if tutorial.lower() == "yes":
                print("You have 6 chances to guess a 5 letter word. You will be able to see what letters you guess correct and if they are in the correct position.")
            break

def playGame():
    
    playing = True
    welcome() 
    while playing:
        
        answer = correctAnswer()
        correctLetters = ""
        incorrectLetters = ""
        correctPlaces = ["-","-" ,"-" ,"-" ,"-"]
        
        for i in range(6):
            print("\n####################################################")
            
            while True:
                guess = getGuess("Input Guess " +str(i+1) + ": ")
                validLength = validLen(guess)
                validWord = validWords(guess)
                if validLength == True and validWord == True:
                    break
                
            if guess == answer:
                playing = gameEnd(f"You win! Answer was: {answer}")
                break
            else:
                correctPlaces, correctLetters, incorrectLetters = workOutPlaces(guess, answer, correctLetters, incorrectLetters, correctPlaces)
                print(f"Correct Places = {str(correctPlaces)}")
                print(f"Correct Letters = {correctLetters}")
                print(f"Incorrect Letters = {incorrectLetters}")
            if i == 5:  #needed so the loop can end preemptively if the answer is found
                if guess != answer:
                    playing = gameEnd(f"You lose! Answer was: {answer}")
                    break     
   
    print("Thank you for playing!")
    quit()
playGame()
