import re

lines_input = []
lines_output = ''
num = int(input())
for i in range(num):
    lines_input.append(input())
for j in lines_input:
    inx = j.find(',', j.find(',') + 1)
    if not re.search(j[:inx], lines_output):
        lines_output += j + '\n'
lines_output = lines_output.strip()
print(lines_output)