import sys

input_data = sys.stdin.read().split('\n')
num = int(input_data.pop(0))
data = []
pooled_data = []
sorted_data = []
result = []
sorted_result = ''
for i in range(num):
    if input_data[i]:
        data.append(input_data[i].split(','))
num_lines = len(data)

for i in range(num_lines):
    pooled_data += data[i]
for i in pooled_data:
    if num_lines == pooled_data.count(i) and (int(i) not in result):
        result.append(int(i))
result.sort()
for i in result:
    sorted_result += str(i) + ','
sorted_result = sorted_result.strip(',')
print(sorted_result)