import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

rock_paper_scissors_list = [rock, paper, scissors]
rock_paper_scissors_name = ["rock", "paper", "scissors"]

print("Welcome to play Rock, Paper, Scissors")

user_input = input("What will you chose? Rock, Paper or Scissors\n")

print(f"You chose {user_input}")

if user_input =="rock":
    print(rock)
elif user_input == "paper":
    print(paper)
elif user_input == "scissors":
    print(scissors)
else:
    print("Not a valid input. Try agin")


list_length = len(rock_paper_scissors_list) -1

rand_item =random.randint(0,list_length)
computers_choice = rock_paper_scissors_name[rand_item]
print (f" Computer chose {computers_choice}")
print(rock_paper_scissors_list[rand_item])


if user_input == computers_choice:
    print("It's a Tie")
elif user_input == "scissors" and computers_choice == "paper":
    print("Scissors beats paper. You win!")
elif user_input == "rock" and computers_choice == "scissors":
    print("Rock beats scissors. You win!")
elif user_input == "paper" and computers_choice == "rock":
    print("Paper beats rock. You win!")
else:
    print("Computer won! You lost! better luck next time")


