# 1. Print each character in the string "Python"
string = "Python"
for char in string:
    print(char)
# 2 Write a loop to count the number of vowels in the string "data science".
string = "data science"
vowels = "aeiou"
vowel_count = 0

for char in string:
    if char in vowels:
        vowel_count += 1

print("Number of vowels: ",vowel_count)

# 3. Write a loop to reverse the string "hello world" and print the reversed string.
string = "hello world"
reversed_string = ""

for char in string:
    reversed_string = char + reversed_string

print("String reversed: ", reversed_string)

# 4. Write a loop to print the ASCII value of each character (search ord() function) in the string "coding".
string2 = "coding"

for char in string2:
    print(f"The ASCII value of {char} is {ord(char)}")

# 5. Write a loop to count the number of times the character "e" appears in the string "experience".
string3 = "experience"
e_count = 0

for char in string3:
    if char == 'e':
        e_count += 1

print("Number of times letter 'e' is repeated: ", e_count)

# 6. Write a loop to replace each vowel in the string "education" with an asterisk (*).
string4 = "education"
vowels = "aeiou"
new_string = ""

for char in string4:
    if char in vowels:
        new_string += "*"
    else:
        new_string += char

print(new_string)

# 7. Write a loop to print every second character in the string "looping".
string5 = "looping"

for i in range(0, len(string5), 2):
    print(string5[i],'\n', end="")

# 8. Write a loop to find the first repeating character in the string "swiss".
string6 = "swiss"
seen = set()

for char in string6:
    if char in seen:
        print(f"The first repeating character is {char}")
        break
    seen.add(char)

# 9. Write a loop to capitalize each word in the string "machine learning is fun".

string7 = "machine learning is fun"
words = string7.split()
capitalized_words = []

for word in words:
    capitalized_words.append(word.capitalize())

print(" ".join(capitalized_words))

# 10. Write a loop to check if the string "racecar" is the same forwards and backwards (ignore case).
string8 = "racecar"
lower_string = string8.lower()

if lower_string == lower_string[::-1]:
    print("The string8 is a palindrome.")
else:
    print("The string is not a palindrome.")