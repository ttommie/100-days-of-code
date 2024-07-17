# Show treasure box ascii art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     '"=.|                  |
|___________________|__"=._o'"-._        '"=.______________|___________________
          |                '"=._o'"=._      _'"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; '"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .' ' '' ,  '"-._"-._   ". '__|___________________
          |           |o'"=._' , "' '; .". ,  "-._"-._; ;              |
 _________|___________| ;'-.o'"=._; ." ' ''."' . "-._ /_______________|_______
|                   | |o;    '"-.o'"=._''  '' " ,__.--o;   |
|___________________|_| ;     (#) '-.o '"=.'_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      '".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Print welcome message
print('Welcome to Treasure Island.\n Your mission is to find the treasure.')

# Print first choice w/ input
plrInput = input('You\'re at a cross road. Where do you want to go: ("left" or "right")\n')

# Check choice of users first answer
if plrInput.upper() == 'LEFT':
  plrInput = input('''\nYou\'ve come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across.\n''')
else:
  print('You fell into a hole. Game Over.')
  exit()
  
# Check choice of users second answer
if plrInput.upper() == 'WAIT':
  plrInput = input('''\nYou arrive at the island unharmed. There is a house with 3 doors.
One "red", one "yellow" and one "blue". Which colour do you choose?\n''')
else:
  print('You get attacked by an angry trout. Game Over.')
  exit()

# Check choice of users third answer
if plrInput.upper() == 'RED':
  print('\nIt\'s a room full of fire. Game Over.')
elif plrInput.upper() == 'BLUE':
  print('\nYou enter a room of beasts. Game Over.')
elif plrInput.upper() == 'YELLOW':
  print('\nYou found the treasure! You Win!')
else:
  exit()