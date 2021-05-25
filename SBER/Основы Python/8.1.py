name = 'Abraсadabra'

print(name[2])
print(name[len(name) - 2])
print(name[0:5])
print(name[0:len(name) - 2])

for i in range(0, len(name)):
    if i == 0:
        print(name[i], end='')
    elif (i % 2) == 0:
        print(name[i], end='')
print()

for i in range(0, len(name)):
    if i == 0:
        continue
    elif (i % 2) != 0:
        print(name[i], end='')
print()

lenName = len(name)
newName = ''
while lenName >= 1:
    newName += name[lenName - 1]
    lenName -= 1
print(newName)

lenName = len(name)
newName = ''
while lenName >= 1:
    newName += name[lenName - 1]
    lenName -= 2
print(newName)
