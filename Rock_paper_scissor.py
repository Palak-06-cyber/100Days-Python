import random

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

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

if user_choice > 2 or user_choice < 0:
    print("Invalid choice!")

computer_choice = random.randint(0,2)
if computer_choice == 0:
    print(f"Computer chose:\n {rock}")
elif computer_choice == 1:
    print(f"Computer chose:\n {paper}")
else:
    print(f"Computer chose:\n {scissors}")

if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
    print("Computer wins!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 1 and computer_choice == 0:
    print("You win!")
elif user_choice == 1 and computer_choice == 2:
    print("Computer wins!")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins!")
elif user_choice == 2 and computer_choice == 1:
    print("You win!")

