n = 4
w = n * 2 - 1
ar = []

for y in range(w):
    ar.append([])
    for x in range(w):
        d = n - abs(x + 1 - n) - abs(y + 1 - n)
        ar[y].append(d if d > 0 else " ")

for i in ar:
    print(*i, sep='')
