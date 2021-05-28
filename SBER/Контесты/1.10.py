import sys
import datetime
import re

def to_time(date):
    date = re.sub('[-T:]', ',', date).split(',')
    for i in range(len(date)):
        date[i] = int(date[i])
    formated_date = datetime.datetime(date[0], date[1], date[2], date[3], date[4])
    return formated_date


input_data = sys.stdin.read().split('\n')
num = int(input_data.pop(0))
data = []

for i in range(num):
    if input_data[i]:
        scheduled_departure, scheduled_arrival, actual_departure, actual_arrival = map(str, input_data[i].split(','))
        scheduled_departure = to_time(scheduled_departure)
        scheduled_arrival = to_time(scheduled_arrival)
        actual_departure = to_time(actual_departure)
        actual_arrival = to_time(actual_arrival)
        if scheduled_departure > actual_departure:
            departure = (scheduled_departure - actual_departure).seconds
        else:
            departure = (actual_departure - scheduled_departure).seconds

        if scheduled_arrival > actual_arrival:
            arrival = (scheduled_arrival - actual_arrival).seconds
        else:
            arrival = (actual_arrival - scheduled_arrival).seconds
        result = arrival + departure
        print(result)

