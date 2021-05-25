lst = [-5, 5, 10]
lstCopy = lst.copy()
last = len(lst) - 1
newLst = []
lstCopy.sort()
sm = lst.index(lstCopy[0])
big = lst.index(lstCopy[last])
lst[sm], lst[big] = lst[big], lst[sm]
print(lst)
