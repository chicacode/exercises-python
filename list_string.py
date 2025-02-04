# Data types: int, string, float, list, tuples, dictionaries, boolean etc.
# String is a data type - a sequence of characters

# index: Positions starts from 0

city = "Vancouver"
print(city[0])
print(city[len(city)  - 1])

# how to get a substring - slice
print(city[0:3])
print(city[3:5])
print(city[:2]) # Va
print(city[2:]) # ncouver

# String methods

lang = "Python"
print(lang.lower())

# String operations
s1 = "Hello "
s2 = "Geri in Python"

print(s1 + s2) # concatenate
print(s1 * 3) # repeat numbers of times

# string formatting

message = s1 + ", " + s2 + ". Welcome to Python course"
print(message)

f_message = f'{s1}, {s2}. Welome to formatting class string in CICCC with Derrick'
print(f_message)

#List - [] a sequence/order of values, data, elements.

listOfCities = ['Vancouver', 'Victoria', 'Burnaby', 'Richmond', 'Surrey', 'Langley']
print(listOfCities)
print(listOfCities[0])
print(listOfCities[-1])
# list methods

listOfCities.append('New West')
listOfCities.append('North Vancouver')
listOfCities.append('West Vancouver')
print(listOfCities)
print(len(listOfCities))
listOfCities.remove('Richmond')
listOfCities.pop(2) # by index

print(listOfCities)
print(len(listOfCities))
# list operation

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l3)
print(l1 * 2)

# list comprehension
# create a list of elements integer from 1 to 10

listOfNumbers = [i for i in range(1, 10)]
print(listOfNumbers)

nums = []
for i in range(1, 34):
    nums.append(i * i)
print(nums)


