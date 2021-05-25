def is_bigger(num1, num2, eps):
    eps = eps / 100 * 99
    return num1 - num2 >= eps


result = is_bigger(1.0, 0.9, 0.1)
print(result)
