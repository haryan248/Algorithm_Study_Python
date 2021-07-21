import sys
tc = int(sys.stdin.readline())
x = []

for i in range(tc):
    a, b = map(int, sys.stdin.readline().split())
    x.append([a, b])

x.sort()
for i in range(tc):
    print(x[i][0], x[i][1])
