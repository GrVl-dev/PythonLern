dct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
getFnd = input('Введите значение: ')

for i, j in dct.items():
    if str(j) == getFnd:
        print(i)
