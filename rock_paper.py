'''
cases: 

A - Rock
Rock-Rock : tie
Rock-paper : paper win
Rock-scissor: rock win

B - Paper
Paper-Paper : tie
Paper - scissor : scissor win
Paper - rock : paper win

C - Scissor
Scissor - Scissor : tie
Scissor - rock : rock win
Scissor - paper : scissor win

'''

import random
items = ['rock', 'paper', 'scissor']
computer = random.choice(items)

user = input("Enter your choice(rock/paper/scissor): ")

print(f"User choice : {user}\nComputer choice : {computer}")

if user == computer :
    print("Match Tie. Play Again!")

elif user == "rock" :
    if computer == "paper":
        print("Computer Win")
    else:
        print("User win")


elif user == "paper":
    if computer == "scissor":
        print("Computer win")
    else:
        print("User win")

elif user == "scissor":
    if computer == "rock":
        print("Computer win")
    else:
        print("User win")
