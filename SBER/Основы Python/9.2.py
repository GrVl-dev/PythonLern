lst = [1, 5, 1, 5, 1]
ln = len(lst)
newLst = []
for i in range(0, ln):
    if i > 0 and lst[i] > lst[i - 1]:
        newLst.append(lst[i])
print(newLst)