import sys

input_data = sys.stdin.read().split('\n')
flight_ids = input_data.pop(0).split(',')
num = int(input_data.pop(0))

for i in range(num):
    if input_data[i]:
        data = input_data[i].split(',')
        for j in flight_ids:
            if int(j) == int(data[1]):
                print(input_data[i])
