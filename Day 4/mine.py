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

game_images = [rock, paper, scissors]
# choice1 = print(input("What do you choose? Type '0' for Rock, '1' for Paper, and '2' for Scissors."))
# computer = random.randint(0,2)
# if choice1 == 0:
#     computer1 = print(f" Computer chose: {computer}")
#     if computer1 == choice1:
#         print("You win!")
#     else:
#         print("You lose!")
# elif choice1 == 1:
#     computer2 = print(f" Computer chose: {computer}")
#     if computer2 == choice1:
#         print("You win!")
#     else:
#         print("You lose!")
# elif choice1 == 2:
#     computer3 = print(f" Computer chose: {computer}")
#     if computer3 == choice1:
#         print("You win!")
#     else:
#         print("You lose!")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])
computer = random.randint(0,2)
print("Computer chose:")
print(game_images[computer])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
elif user_choice == 0 and computer == 2:
    print("You win!")
elif computer == 0 and user_choice == 2:
    print("You lose!")
elif computer > user_choice:
    print("You lose!")
elif computer < user_choice:
    print("You win!")
else:
    print("It's a tie!")




