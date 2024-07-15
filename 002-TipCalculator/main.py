# Print a greeting message
print('Welcome to the tip calculator!')

# Ask for the amount on the bill
billAmt = float(input('What was the total bill:'))

# Ask for the tip amount on the bill
tipAmt = int(input('What percent of tip would you like to give:'))

# Ask for the amount of people to split the bill with
peopleAmt = int(input('How many people to split the bill:'))

# Calculate total amount of bill
totalAmt = (billAmt * (tipAmt / 100)) + billAmt

# Calculate between amount of people
perPersonAmt = totalAmt / peopleAmt

# Print results
print(f'Total Bill Amount: {round(totalAmt, 2)}')
print(f'Per Person Amount: {round(perPersonAmt, 2)}')