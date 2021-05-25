lst = [7, 8, 9, 6, 54]
newLst = []
lnInx = len(lst)
for i in range(0, lnInx):
    if i == 0 or i % 2 == 0:
        newLst.append(lst[i])
print(newLst)