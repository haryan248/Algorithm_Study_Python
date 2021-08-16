import sys
input = sys.stdin.readline
n = int(input())
a=[]
for i in range(n):
    a.append(list(map(int, input().split())))

a.sort(key=lambda x: (x[1], x[0]))
cnt=0
start=0
for i in a:
    if i[0] >=start:
        start = i[1]
        cnt+=1

print(cnt)
