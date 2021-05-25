spk = ['abc', 'abc', 'abc']
dct = {}
for i in range(0, len(spk)):
    count = dct.get(spk[i])
    if not count:
        dct.update({spk[i]: 1})
    elif count >= 1:
        count += 1
        dct.update({spk[i]: count})
print(dct)
