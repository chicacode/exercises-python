# 1. List Creation and Access
# Create a list with the following elements: 1, 2, 3, 4, 5. Print the third element in the list.

my_list = [1, 2, 3, 4, 5]
print("third element in the list", my_list[2])  # Output: 3

# 2. Append the number 6 to the list
my_list.append(6)
print(my_list)
del my_list[1]
print(my_list)  # Output: [1, 3, 4, 5, 6]

# 3. List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[:5])  # Output: [10, 20, 30, 40, 50]
print(numbers[-3:])  # Output: [80, 90, 100]
print(numbers[::2])  # Output: [10, 30, 50, 70, 90]



# 4. List Operations: Create a list of numbers from 1 to 10
num_list = list(range(1, 11))

print(sum(num_list))  # Output: 55

# Find the maximum and minimum values
print(max(num_list))  # Output: 10
print(min(num_list))  # Output: 1

# 5. List comprehension to create a list of squares from 1 to 10
squares = [x**2 for x in range(1, 11)]
print(squares)
def squares(start, end):
    return [i**2 for i in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]

# 6. Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access the element 5 from the nested list
print(nested_list[1][1])  # Output: 5

