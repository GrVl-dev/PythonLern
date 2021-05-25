n = 5

for i in range(1, n + 1):
    count = n - i + 1
    row = ''
    while count > 1:
        row += ' '
        count -= 1
    print(row, end='')
    for j in range(1, i + 1):
        print(j, end='')
    while j > 1:
        print(j - 1, end='')
        j -= 1
    print()
