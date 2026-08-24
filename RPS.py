import random

Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input(
    "What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "
))

computer_choice = random.randint(0, 2)

print(f"Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a Draw!")

elif user_choice == 0 and computer_choice == 2:
    print("You Win!")

elif user_choice == 1 and computer_choice == 0:
    print("You Win!")

elif user_choice == 2 and computer_choice == 1:
    print("You Win!")

elif user_choice in [0, 1, 2]:
    print("You Lose!")

else:
    print("You typed an invalid number. You Lose!")
