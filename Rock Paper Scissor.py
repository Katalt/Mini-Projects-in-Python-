# Rock Paper Scissor Game

import random

def play():
    score_user = 0
    score_computer = 0
    best_of_three = 0

    for i in range(0,3):
        user = input("for Rock put'r', for Paper put 'p', for Scissor put 's': ")
        computer = random.choice(['r','p','s'])
        if user == computer:
            print("Computer choice: ",computer)
            print("it is a tie\n")
            best_of_three += 1
            
        elif (user == 'r' and computer == 's' or
              user == 'p' and computer == 'r' or
              user == 's' and computer == 'p'):
              print("Computer choice: ",computer)
              print("You won\n")
              best_of_three += 1
              score_user += 1
        else:
            print("Computer choice: ",computer)
            print("you lost\n")
            best_of_three += 1
            score_computer +=1

    if best_of_three == 3:
        print("Game over")
        print("Score of user: ",score_user)
        print("Score of computer: ",score_computer)
        if score_user > score_computer:
            print("User has won")
        elif score_user < score_computer:
            print("Computer has Won")
        else:
            print("It is a tie between computer and user")
play()
