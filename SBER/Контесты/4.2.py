result = []
for i in range(100000):
    num = '13'
    if str(i).find(num) == -1:
        result.append(i)
print(len(result))
