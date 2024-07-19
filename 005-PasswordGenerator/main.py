# Import random module
import random

# Set data types to use in password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
          'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
          'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
          'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print welcome message
print("Welcome to the PyPassword Generator!")

# Ask user for specific options when generating password
passwordLength= int(input("How many letters would you like in your password?\n")) 
passwordSymCount = int(input(f"How many symbols would you like?\n"))
passwordNumCount = int(input(f"How many numbers would you like?\n"))

# Generate password using loops
easyPassword = ''

for i in range(1, passwordLength + 1):
  easyPassword += random.choice(letters)

for i in range(1, passwordSymCount + 1):
  easyPassword += random.choice(symbols)

for i in range(1, passwordNumCount + 1):
  easyPassword += random.choice(numbers)

# Print easy password results
print(f'Easy Level Password: {easyPassword}')
      
# Scramble all letters, numbers & symbols
hardPassword = ''.join(random.sample(list(easyPassword), len(list(easyPassword))))

# Print hard password results
print(f'Hard Level Password: {hardPassword}')