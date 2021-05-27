import sys

input_data = sys.stdin.read().split('\n')
num = int(input_data.pop(0))
data = []
sorted_data = []
for i in range(num):
    data.append(input_data[i].split(','))
data.sort(key=lambda j: j[1])
for i in range(len(data)):
    print(data[i][1])
