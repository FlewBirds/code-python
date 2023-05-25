
import random


computer_choice = random.choice(['scissors', 'rock', 'paper'])

user_choice: str = input("Do you want - rock, pacper, or scissors?\n")

if computer_choice == user_choice:
    print("TIE", "computer_choice :", computer_choice)
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('WIN', "computer_choice :", computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN', "computer_choice :", computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN', "computer_choice :", computer_choice)
else:
    print('you lose: (computer win)', computer_choice)
#####################

