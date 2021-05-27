import sys

input_data = sys.stdin.read().split('\n')
num = int(input_data.pop(0))
data = []
sorted_data = []
for i in range(num):
    if input_data[i]:
        data.append(input_data[i].split(','))

data.sort(key=lambda i: int(i[1]))
result = {}
for j in range(len(data)):
    if data[j][1] not in result.keys():
        result[data[j][1]] = [data[j][3]]
    else:
        result[data[j][1]].append(data[j][3])
    if len(result) > 1:
        print(data[j-1][1])
        print(','.join(result[data[j-1][1]]))
        result.pop((data[j-1][1]))
    if j == len(data) - 1:
        print(data[j][1])
        print(','.join(result[data[j][1]]))

