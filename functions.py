# February, 4, 2025
# functions: Reusable block of code

# 1. Define a Function
def print_hello(n):
    for i in range(n):
        print("I am learning python now")


# 2. Function Basics: Write a function called greet that takes a name as an argument and prints a greeting message with that name.
def greetName(name):
    return f"Hello, dear {name}"


# 3. Return Values: Create a function square that takes an integer and returns its square.
def square(n):
    """Returns the square of the given number."""
    return n ** 2


# 4. Multiple Parameters: Write a function add that takes two numbers as parameters and returns their sum.
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


# 5. Default Parameters: Write a function greet_user that greets the user with a default name if no name is provided. The default name should be "Guest".
def greet_user(name="Guest"):
    """Greets the user with a default name if none is provided."""
    return f"Hello, {name}!"


# 6. Keyword Arguments: Write a function format_address that takes street, city, and country as keyword arguments and returns a formatted address string.
def format_address(street, city, country):
    return f"{street}, {city}, {country}"


# 6.1. Docstrings: Create a function factorial that calculates the factorial of a given number and includes a docstring explaining the function.
def factorial(num):
    # single line to find factorial
    return 1 if (num == 1 or num == 0) else num * factorial(num - 1)


number = 5


# 7.  Calculate BMI: Write a function calc_bmi that takes 2 numbers (height and weight) and returns the bmi.
def calc_bmi(height, weight):
    # height (m) - weight (kg)
    """"
    This retun the calculation
    """""
    return weight / (height * height)


# 8. Simple Arithmetic: Write a function multiply that takes two numbers as parameters and returns their product.
def multiply(num1, num2):
    return num1 * num2


# 9. String Manipulation: Write a function reverse_string that takes a string as an argument and returns the reversed string.

def reverse_string(sentence):
    reversed_sentence = " ".join(sentence.split()[::-1])
    return reversed_sentence


# 10. Boolean Functions: Write a function is_even that takes an integer and returns True if the number is even and False otherwise.

def is_even(number):
    if number == 0:
        print("Zero")
    return number % 2 == 0


# 11. List Operations: Write a function sum_list that takes a list of numbers and returns the sum of the list.

def sum_list(list):
    total = 0

    # Iterate through the list and add each number to the total
    for num in list:
        total += num

    return total


# 12. Count Occurrences: Write a function count_vowels that takes a string and returns the number of vowels in the string.

def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    count = sum(1 for char in sentence if char in vowels)
    return count


# 13. Find Maximum: Write a function find_max that takes three numbers and returns the maximum of the three.
def find_max(num1, num2, num3):
    """Returns the maximum of the three given numbers."""
    return max(num1, num2, num3)


# 14. Palindrome Check: Write a function is_palindrome that takes a string and returns True if the string is a palindrome and False otherwise.
def is_palindrome(text):
    # Return true if palindrome
    s = text.lower().replace(" ", "")  # Convert to lowercase & remove spaces
    return s == s[::-1]


# 15. Temperature Conversion: Write a function celsius_to_fahrenheit that takes a temperature in Celsius and returns the temperature in Fahrenheit.
def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


# 2. Call: Execution/Invoke of the function

print("Print function")
print_hello(1)
print(calc_bmi(1.80, 70))
print(greetName("Geri"))
print(add(5, 10))
full_adress = format_address("1290 Alberni ST", "Vancouver", "Canada")
print(full_adress)
print("Square: ", square(4))
print(greet_user())
print(greet_user("Alice"))
print(f"Factorial of {number} is: ", factorial(number))
print("The product of ultiply is: ", multiply(7, 8))
reversedTxt = reverse_string("I Love Python")
print("Reversed: ", reversedTxt)
print("Is EVEN?: ", is_even(4))
print("Sum result:", sum_list([9, 9, 9, 3, 3, 3, 6, 6, 6]))
print("Sum vowels: ", count_vowels("I love these clases"))
print(find_max(10, 25, 7))
print(find_max(-5, 0, 3))
print("Is palindrome: ", is_palindrome("racecar"))
print("Is palindrome: ", is_palindrome("hello"))
print("Is palindrome: ", is_palindrome("madam"))
print("convert celsius to farenheit: ", celsius_to_fahrenheit(0))
print("convert celsius to farenheit: ", celsius_to_fahrenheit(25))
print("convert celsius to farenheit: ", celsius_to_fahrenheit(-10))
print("convert celsius to farenheit: ", celsius_to_fahrenheit(100))
