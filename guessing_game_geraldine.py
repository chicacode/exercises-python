# Vancouver, February 6, 2025
# Guessing Game in Python
# Instructor: Derrick
# Student: Geraldine

# In this lab, you’re going to create your first game, called “guessing game”.
# Your job is to complete the program from the given starter python file.

from random import randint

"""" 1. Your program should generate a random number between 1 and 1000.
     The code for this step is provided. """

"""  2. Input from user: check user's input
You need to handle all possible errors.
You need to update the range every time. """

""" 3. Your program should respond with an appropriate message. """

""" 4. Your program should keep track of the number of 
guesses made by the user. (10 guesses max)  """

lower = 1
higher = 1000
max_of_guesses = 10
count = 0
answer = randint(lower, higher)
#print(answer)

while count < max_of_guesses:
    try:
        guess = int(input(f"Welcome to Guessing Game - Guess a number from {lower} - {higher}:  "))
        if lower <= guess <= higher:
            count += 1
            print(count)
            if guess < lower or guess > higher:
                print(f"'️Please guess within the range {lower} - {higher}. Try again.")
                continue
            if guess < answer:
                print('To low! try again')
                lower = guess + 1
            if guess > answer:
                print('To high! try again')
                higher = guess - 1
            if guess == answer:
                print(f"Congratulations! The hidden number is: {answer} - You guess the number in {count} times")
                break
        else:
            print('Please, enter from {lower} - {higher}')
    except ValueError:
        print('Please enter a number')
        continue
else:
    print(f"Sorry, You have used {max_of_guesses}, You've lost!, the hidden number was {answer}")

