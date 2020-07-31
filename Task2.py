from random import randint

characters = [randint(1, 40) for i in range(20)]
print(characters)

a = int(input("Enter index in list : "))
b = int(input("Enter value in list : "))

characters.append(0)
for i in range(len(characters) - 1, a, -1):
    characters[i] = characters[i - 1]
characters[a] = b
print(characters)
