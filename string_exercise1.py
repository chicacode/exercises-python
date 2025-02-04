# 1. String Creation and Access
# Create a string with the value "Hello, World!". Print the first and last character of the string.

txt1 = "Hello, World!"
print("First character", txt1[0])
print("Last character", txt1[-1])

#2. String Slicing
# Given the string "Python Programming", print the substring "Python".
# Print the substring "Programming".

txt2 = "Python Programming"
print("Print the substring", txt2[:6]) # Slicing operator is called this [:6]
print("Print the substring", txt2[7:]) # [:]

# 3. String Methods
# Convert the string "hello, world!" to uppercase and print it.
# Replace "World" with "Python" in the string "Hello, World!" and print the updated string.

txt3 = "hello, world!"

print(txt3.upper())

newTxt3 = txt3.replace("world", "Python")

print(newTxt3.capitalize())

# 4. String Concatenation
# Concatenate the strings "Hello" and "World" with a space in between. Print the result.

txt4 = "Hello"
txt5 = "Geri in Pthon World"

print(txt4 + " " + txt5)

# 5. String Splitting
#Given the string "apple,banana,cherry", split it by commas and print the resulting list.

strFruits = "apple, banana, cherry"
listFruits = strFruits.split(",")
print(listFruits)

# 6. String Formatting
# Use string formatting to create a string that says "My name is [name] and I am [age] years old", where [name] and [age] are variables. Print the result.

name = "Geri"
age = "Ageless"

f_user = f"My name is {name} and I am {age} years old"
print(f_user)

# 7. String Reversal
# Write a program that takes a string input from the user and prints the string in reverse order.

string = input("Users input: ")

# def is short for “define”. It's a keyword that you need to define a function (aka method)
def reverse_slicing(s):
    return s[::-1]
print('Reverse String using slicing =', reverse_slicing(string))

# s[::-1] the colon takes all elemnt in string and then other colon : takes backwards

# Bonus Exercises
#
# 1. Palindrome Check
# Write a function that checks whether a given string is a palindrome (reads the same forwards and backwards). Test it with the strings "madam" and "hello".
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


print(is_palindrome("madam"))  # True
print(is_palindrome("hello"))  # False

# 2. List to String Conversion
# Convert the list ['P', 'y', 't', 'h', 'o', 'n'] to a single string "Python". Print the result.

# List of characters
char_list = ['P', 'y', 't', 'h', 'o', 'n']
char_list2 = ['J', 'a', 'v', 'a', 's', 'c', 'r', 'i', 'p', 't']

# Convert list to string
# joining all the elements using join method with string
result = ''.join(char_list)
result2 = ''.join(char_list2)
# Print the result
print(result + " " + "is" +  " " + "better" + " " + "than" + " " +  result2 )