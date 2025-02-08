# Vancouver, February 7 2025
# Data Science Python Class
# Instructor Derrick
# Student Geraldine

# Lab 2

"""""
Question: How can I use mod (%) and integer division (/) 
to figure out the nth digit of anInteger?
"""""
from guessing_game_geraldine import count

""" stack overflow 
https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
"""

"""
As an example, if I have number = 123456, I want to be able to use mod and division in some
way to fetch the 1st digit of this number (which is 6), or 2nd (which is 5), or 3rd (which is 4),
etc. using some equation that involves the values of "number" and "n".

"""
# Inputs User
user_number = int(input('Enter a number:'))
user_n = int(input('Enter second number:'))

# Copy of the number
temp = user_number
count = 1
# Check errors
if user_n <= 0:
    print('Enter a valid number, greater than 0')
elif user_n > len(str(user_number)):
    print('Position is out of range')
else:
    while count < user_number:
        temp = temp // 10
        count = count + 1
    nth_digit = temp % 10
    print(f"The {user_n}th digit from the right is: {nth_digit}")

print('N1: ', user_number)
print('N2: ', user_n)

