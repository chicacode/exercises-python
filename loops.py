# Loops:  are a programming construct that allows a blok of code be repeated a x number times, it is used in list and objects, dictionaries to oterates through different elements inside a list data structure.
## Are use for iterate over a sequences

# For Loop
# While Loop

for i in range(5):
    print(i)

for x in range(10, 20):
    print(x)

for i in range(11, 20, 2):
    print(i)

# Sequence of characters

word = "Hi again"
for s in word:
    print(s)

for i in range(len(word)):
    print(word[i])

list = [10, 20, 30]
for i in list:
    print("inside the list ", i)

for i in range(len(list)):
    print("looping the range list ", list[i])

# While loop
# while true ... repeat.
i = 0
while i < 10:
    print("I'm here again")
    i += 1


