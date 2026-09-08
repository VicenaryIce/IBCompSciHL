
import random
import math
from unicodedata import numeric
guesses = 0
guesslist = []
def create_number(start,range):
    num = random.randint(start,range)
    return num

def eval_guess(guess,number):
    global guesses
    if guess == number:
        guesses+=1
        if guesses ==1:
            print("You got this correct in one guess!")
        else:
            print("Correct")
        guesslist.append(guesses)
        return True
    elif guess > number:
        print("The number is less than your guess")
        guesses +=1
        return False
    elif guess <number:
        guesses +=1
        print("The number is greater than your guess")
        return False


def play_again(answer):
    if answer[0].lower() =='y':
        return True 
    else:
        return False 
def eval_stats(guesslist,returnType):
    if returnType =="Playing again":
        print("Guesses this game: ", str(guesslist[-1]))
        print("Total games: ",str(len(guesslist)))
    if returnType == "Ending play":
        for i in guesslist:
            sum +=i
        print("Total guesses: ",str(sum))
        


def run_game():
    num  = create_number(0,100)
    print(num)
    guess = eval_guess(int(input("Enter the number you are guessing")),num)
    while not guess:
        guess = eval_guess(int(input("Guess please")),num)
    if play_again(input("Would you like to play again")):
        print("Playing again")
    else:
        print("Not playing again")

run_game()