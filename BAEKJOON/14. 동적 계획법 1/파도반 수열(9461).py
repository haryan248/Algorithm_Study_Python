import sys
input = sys.stdin.readline
T = int(input())

def triangle(N):
	if N == 1 or N==2 or N==3:
		return 1
	dp = [0*i for i in range(N+1)]
	dp[1] = 1
	dp[2] = 1
	dp[3] = 1
	
	for k in range(3, N+1): 	
		dp[k] = dp[k-2] + dp[k-3]
	return dp[N]

for i in range(T):
	N = int(input())
	print(triangle(N))