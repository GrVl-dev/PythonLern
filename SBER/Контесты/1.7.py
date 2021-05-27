data_input = []
result = ''
flight_ids = input().split(',')
num = int(input())
for i in range(num):
    data_input.append(input().split(','))
    for j in flight_ids:
        if j in data_input[i][1]:
            result += ','.join(data_input[i]) + '\n'
result = result.strip()
if result:
    print(result)
