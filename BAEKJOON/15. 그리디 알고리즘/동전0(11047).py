import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a=[]
for i in range(n):
	a.append(int(input()))
cnt = 0
for i in range(n-1,-1,-1):
	if a[i] <= k:
		cnt += k//a[i]
		k %=a[i]

print(cnt)