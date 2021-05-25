lines_input = []
lines_output = ''
num = int(input())
for i in range(num):
    lines_input.append(input())

for i in lines_input:
    line = i.split(',')
    line[2] = line[2].replace('Номер:', '')
    if line[3].find(';') == -1:
        seat_no = line[3]
        symbol = seat_no[-1:]
        seat_no = seat_no.strip(symbol)
        line[3] = seat_no + ';' + symbol
    lines_output += ','.join(line) + '\n'
lines_output = lines_output.strip()
print(lines_output)
