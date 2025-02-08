# Data Science Python Class
# Instructor Derrick
# Student Geraldine

# Lab 2
""" Part 1: Modulus and Integer division
Question: How can I use mod (%) and integer division (/) 
to figure out the nth digit of an Integer?

Test:
As an example, if I have number = 123456, I want to be able to use mod and division in some
way to fetch the 1st digit of this number (which is 6), or 2nd (which is 5), or 3rd (which is 4),
etc. using some equation that involves the values of "number" and "n".
"""

# Inputs User
user_number = int(input('Enter a number:'))
user_n = int(input('Enter second number - Position:'))

# Copy of the number
temp = user_number
count = 1
# Check errors
if user_n <= 0:
    print('Enter a valid number, greater than 0')
elif user_n > len(str(user_number)):
    print('Position is out of range')
else:
    # Loop count over the n
    while count < user_n:
        # Remove last digit
        temp //= 10
        # move one
        count += 1

    # Mod 10
    nth_digit = temp % 10
    print(f"The {user_n}th digit from the right is: {nth_digit}")

"""
Part 2: Star Drawings with Nested Loops

Take a look at starry.py posted on our course website. Take some time looking through the
code, explaining how it works.
Add your explanation as in-line comments if needed.
Once you feel completely confident in your understanding of starry.py, comment out the
given loop and add in other loops which draw at least three of the following drawings (n
should be the # of rows for each of them). If you choose any of the last three, decide what
you want to do it if n is even.

References used: https://pynative.com/print-pattern-python-examples/#h-inverted-pyramid-pattern-of-numbers
Hint:
n = int(input("# rows: "))

# You are only allowed to use the following 3 print functions.
# print()
# print(" ", end="")
# print("*", end="")

# nested loops example
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

"""


# pattern 1

def print_pattern1(n):
    # Print piramid
    for i in range(n):
        spaces = ' ' * (n - i - 1)  # Creates spaces to center the stars
        stars = '*' * (2 * i + 1)  # Creates the pyramid pattern
        print(spaces + stars)


# rows = int(input("Enter the number of rows: "))
# print_pattern1(rows)

# pattern 2
def print_pattern2(n):
    print(n)
    """ One inverted triangle """
    for i in range(n, 0, -1):
        count = "*"  # Create the star
        for j in range(i):
            print(count, end='')  # Add space
        print('\r')


rows = int(input("Enter the number of rows: "))
print_pattern2(rows)

# pattern 3

def print_pattern3(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end='')
        print()
    for i in range(n, 0, -1):
        count = "*"
        for j in range(0, i - 1):
            print(count, end='')
        print('\r')

rows = int(input("Enter the number of rows: "))
print_pattern3(rows)

# pattern 4
# pattern 5
