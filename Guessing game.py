# Guessing the number

import random

def guess_number(x):
    random_number = random.randint(1,x)
    guess = 0
    guess_number = 0 
    guess_max = 3
    if guess != guess_max:
        while guess_number != random_number and guess != 3:
            guess_number = int(input(f'guess a number between 1 and {x}: '))
            guess+=1
            if guess_number < random_number:
                print("Too low")
            elif guess_number > random_number:
                print("Too high")
        if guess == guess_max:
            print("Out of Guesses")
        else:
            print(f'Yay you guessed the number: {random_number}')
        

guess_number(10)
