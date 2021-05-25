data_input = []
data_output = ''
flight_ids = []
fin_flight_ids = []
count = 0
num = int(input())
for i in range(num):
    data_input.append(input().split(','))
    flight_id = data_input[i][1]
    flight_ids.append(flight_id)

print(flight_ids)

