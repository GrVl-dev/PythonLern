lines_input = []
lines_output = ''
num = int(input())
for i in range(num):
    lines_input.append(input())

for i in lines_input:
    line = i.split(',')
    price = line.pop()
    new_price = price.split('.')
    for j in new_price:
        line.append(j)
    lines_output += \
        "Номер бронирования " + line[0] + ", забронирован " \
        + line[1] + ". Цена: " + line[2] + " руб. " + line[3] \
        + " коп.\n"
lines_output = lines_output.strip()
print(lines_output)
