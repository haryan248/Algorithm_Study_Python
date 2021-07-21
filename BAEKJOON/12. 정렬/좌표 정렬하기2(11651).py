import sys
tc = int(sys.stdin.readline())
x = []

for i in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    x.append([b, a])

x = sorted(x)
for i in range(tc):
    print(x[i][1], x[i][0])
