import random
import sys

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Saves images into list
image_list = [rock, paper, scissors]

#Asks for user's choice
user_input = int(input("What do you choose? 0 for Rock, 1 for Paper, and 2 for Scissors\n"))

#generates computer's choice
computer_input = random.randint(0,2)

#prints user's choice
if user_input == 0:
  print("\nYou chose: Rock")
  print(image_list[0])
elif user_input == 1:
  print("\nYou chose: Paper")
  print(image_list[1])
elif user_input == 2:
  print("\nYou chose: Scissors")
  print(image_list[2])
else:
  print("\nYou typed an invalid number.")
  sys.exit()

#prints computer's choice
if computer_input == 0:
  print("\nThe computer chose: Rock")
  print(image_list[0])
elif computer_input == 1:
  print("\nThe computer chose: Paper")
  print(image_list[1])
else:
  print("The computer chose: Scissors")
  print(image_list[2])


#prints winner
if user_input == 0 and computer_input == 1:
  print("Computer won!")
elif user_input == 0 and computer_input == 2:
  print("You won!")
elif user_input == 1 and computer_input == 2:
  print("Computer won!")
elif user_input == 1 and computer_input == 0:
  print("You won!")
elif user_input == 2 and computer_input == 0:
  print("Computer won!")
elif user_input == 2 and computer_input == 1:
  print("You won!")
else:
  print("It's a draw!")
