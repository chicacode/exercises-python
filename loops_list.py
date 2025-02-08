# 1. Write a loop to print each element in the list [10, 20, 30, 40, 50].

greatList = [10, 20, 30, 40, 50]

for val in greatList:
    print(val)

# 2. Write a loop to calculate the sum of all elements in the list [1, 2, 3, 4, 5].
secondList = [1, 2, 3, 4, 5]
# Initialize a variable to hold the sum
res = 0

for val in secondList:
    res += val

print("Sum of the list: ", res)

# 3. Write a loop to find the largest number in the list [3, 7, 2, 9, 4].
thirdList = [3, 7, 2, 9, 4]
print(thirdList)

currentNumber = thirdList[0]
for ele in thirdList:
    if ele > currentNumber:
        print("ele is: ", ele)
        currentNumber = ele
print("The largest number is: ", currentNumber)

# 4. Write a loop to count how many times the number 4 appears in the list [1, 4, 4, 2, 4, 3].

fourList = [1, 4, 4, 2, 4, 3]


def listCounts(nums):
    # Initialize a variable count to keep track of the count of occurrences of the number 4.
    count = 0

    for num in nums:
        if num == 4:
            # If the element is 4, increment the count by 1.
            count = count + 1

    # Return the final count after iterating through the list.
    return count


print("Repeated: ", listCounts(fourList))

# 5. Write a loop to create a new list that contains the squares of each number in the list [1, 2, 3, 4, 5].

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number ** 2)

print(squares)

# 6. Write a loop to concatenate all the words in the list ["Python", "is", "awesome"] into a single string.
words = ["Python", "is", "awesome"]
final_msg = ""
for item in words:
    final_msg += item + " "
print("Words result: ", final_msg)

# 7. Write a loop to create a new list that contains only the even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
seventhList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create a list of even numbers using list comprehension
res = [val for val in seventhList if val % 2 == 0]
print("Even List:", res)

# 8. Write a loop to multiply each number in the list [2, 4, 6, 8] by 2 and store the results in a new list.

eightList = [2, 4, 6, 8]
c = 2

# Multiply each element in the list by the constant using list comprehension
res = [x * c for x in eightList]
print("Each elemnt multiply from the list and return new list", res)

# 9. Write a loop to remove all occurrences of the number 3 from the list [1, 3, 3, 4, 3, 5, 3].
nineList = [1, 3, 3, 4, 3, 5, 3]

# Elements to remove
remove = [3]
# Remove elements using a simple for loop
res = []

for val in nineList:
    if val not in remove:
        res.append(val)

print("new list: ", res)
# 10. Write a loop to find the index of the first occurrence of the number 7 in the list [5, 7, 8, 7, 10].

tenList = [5, 7, 8, 7, 10]

for i in range(len(tenList)): # range length of 5 numbers 0,1,2,3,4
    if tenList[i] == 7:
        print("index of 7", i)
        break

# we can use enumerate() fn that is going to return pair list of index.
# We pass the list inside the enumerate formula.
