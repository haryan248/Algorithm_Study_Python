import sys
n = int(sys.stdin.readline())

li = []
for i in str(n):
    li.append(int(i))

li.sort(reverse=True)  # 내림차순

for i in li:
    print(i, end='')
