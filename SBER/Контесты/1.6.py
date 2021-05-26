def max_list(lst):
    new_list = []
    val = []
    dct = {}
    res = ''
    for j in lst:
        if j not in dct:
            dct[j] = lst.count(j)
            val.append(lst.count(j))
    val.sort(reverse=True)
    for k, v in dct.items():
        if v == val[0]:
            new_list.append(k)
    new_list.sort()
    for n in new_list:
        res += str(n) + ' '
    return res


data_input = []
data_output = ''
flight_ids = []
fin_flight_ids = []
count = 0
num = int(input())
for i in range(num):
    data_input.append(input().split(','))
    flight_id = data_input[i][1]
    flight_ids.append(int(flight_id))

result = max_list(flight_ids)
result = result.strip()
print(result)
