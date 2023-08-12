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

#Write your code below this line 👇
import random

user_choice = int(input("What do you choose? Pick 0 for rock, 1 for paper, and 2 for scissors"))

comp_choice = random.randint(0,2)

print(f"The computer has chosen {comp_choice}")

if user_choice == comp_choice:
  print("It's a draw")
elif(user_choice > comp_choice):
  if(user_choice == 2 and comp_choice == 0):
    print("You lose")
  else:
    print("You win")
elif(user_choice < comp_choice):
  if(user_choice == 0 and comp_choice == 2):
    print("You win")
  else:
    print("You lose")
else:
  print("You chose an invalid number")