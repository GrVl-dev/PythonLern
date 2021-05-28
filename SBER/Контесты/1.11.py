import sys

input_data = sys.stdin.read().split('\n')
num = int(input_data.pop(0))
data = []
status_table = {}
statuses = ['Scheduled', 'On Time', 'Delayed', 'Departed', 'Arrived', 'Cancelled']
for i in range(num):
    if input_data[i]:
        flight_id, status = map(str, input_data[i].split(','))
        if status not in status_table.keys():
            status_table[status] = 1
        else:
            status_table[status] += 1
for i in statuses:
    if i in status_table.keys():
        print(status_table[i])
    else:
        print(0)
