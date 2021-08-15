import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
dp = [0] * 1000
for i in range(n):
	dp[i] = 1
	for j in range(i):
		if a[j] < a[i]:
			dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))