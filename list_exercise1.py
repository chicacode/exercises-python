# 1. List Creation and Access
# Create a list with the following elements: 1, 2, 3, 4, 5. Print the third element in the list.

my_list = [1, 2, 3, 4, 5]
print("third element in the list", my_list[2])  # Output: 3

# 2. Append the number 6 to the list
my_list.append(6)
print(my_list)
del my_list[1]
print(my_list)

# 3. List Slicing
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[:5])
print(numbers[-3:])
print(numbers[1::2])

# 4. List Operations: Create a list of numbers from 1 to 10
num_list = list(range(1, 11))

print(sum(num_list))

# Find the maximum and minimum values
print(max(num_list))
print(min(num_list))

# 5. List comprehension to create a list of squares from 1 to 10

# exponent
# x to the power of two 2 x ** 2
squares = [x ** 2 for x in range(1, 11)]
print(squares)
def squares(start, end):
    return [i**2 for i in range(start, end+1)]

print(squares(2, 3)) # Should be [4, 9]

# 6. Nested Lists
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Access the element 5 from the nested list
print(nested_list[1][1])  # Output: 5

