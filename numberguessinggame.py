from asyncio.runners import run
import math
from multiprocessing import Value
import random 

num = random.randint(0,100)
guesses = 0
totalguesses = 0
games = 0
bestgame =0
def run_game():
    global guess
    global guesses
    global totalguesses
    global num
    global games
    global bestgame
    print(num)
    games +=1
    guesses = 0
    
    guess = input("Guess the number I am thinking of: ")

    while guess !=num:


        try:

            if int(guess)==num:
                guesses = guesses+1
                break

            elif int(guess) > num:
                print("Wrong. Your guess is greater than my number")
                guess = input("Guess the number I am thinking of: ")
                guesses = guesses+1

            elif int(guess) <num:
                print("Wrong. Your guess is less than my number")
                guess = input("Guess the number I am thinking of: ")
                guesses=  guesses+1

        except ValueError:
            print("Please enter an integer for this number ")
            guess = input("Guess the number I am thinking of")
    totalguesses+=guesses

    print("You win")
    print("Guesses this game: ",str(guesses))
    print("Total guesses",str(totalguesses))
    if games ==1:
        bestgame = guesses
    elif games >1:
        if guesses <bestgame:
            bestgame = guesses

    answer = input("Would you like to play again?: ")

    if answer[0].lower() =="y":
        num = random.randint(0,100)
        run_game()
    else:
       print("Total games:",str(games))
       print("Total guesses:",str(totalguesses))
       print("Guesses per game: ",str(round((totalguesses/games),1)))
       print("Best game",bestgame)


run_game()


