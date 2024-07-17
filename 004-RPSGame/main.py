# Import random for cpu choice
import random

# Setup game ascii
rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Setup list to provide proper art for each player
game_images = [rock, paper, scissors]

# Ask user rps choice
usrChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

# Get random cpu choice
cpuChoice = random.randint(0, 2)

while usrChoice != 0 and usrChoice != 1 and usrChoice != 2:
  usrChoice = int(input('Try again...\nWhat do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

# Print game in ascii
print('USER - CPU')
print(game_images[usrChoice])
print('VS\n')
print(game_images[cpuChoice])  
  
# Print winner
if usrChoice != cpuChoice:
  if usrChoice == 0 and cpuChoice == 2 or usrChoice == 1 and cpuChoice == 0 or usrChoice == 2 and cpuChoice == 1:
    print('USER WINS!')
  else:
    print('CPU WINS!')
else:
  print('TIE!')