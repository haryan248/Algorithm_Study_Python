arryx = []
arryy = []
for i in range(3):
    x, y = map(int, input().split())
    arryx.append(x)
    arryy.append(y)

for i in range(3):
    if arryx.count(arryx[i]) == 1:
        rx = arryx[i]
    if arryy.count(arryy[i]) == 1:
        ry = arryy[i]

print("%d %d" % (rx, ry))
