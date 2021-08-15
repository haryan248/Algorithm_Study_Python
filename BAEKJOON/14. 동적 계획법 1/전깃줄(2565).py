import sys
input = sys.stdin.readline
x = int(input())
a=[]
for i in range(x):
	a.append(list(map(int, input().split())))
a.sort(key = lambda x :  x[1])
new_list = list(map(list, zip(*a)))
print(new_list[0])
dp = [0] * 500

for i in range(len(new_list[0])):
	dp[i] = 1
	for j in range(i):
		if new_list[0][j] < new_list[0][i]:
			dp[i] = max(dp[i], dp[j]+1)
print(x - max(dp))
