import sys
input = sys.stdin.readline
n=int(input())
a=[list(map(int,input().split())) for _ in range(n)]
for i in range(1, n):
	for j in range(len(a[i])):
		if j==0:
			a[i][j] += a[i-1][j]
		elif j == len(a[i])-1:
			a[i][j] +=  a[i-1][j-1]
		else:
			a[i][j] += max(a[i-1][j], a[i-1][j-1])
print(max(a[n-1]))