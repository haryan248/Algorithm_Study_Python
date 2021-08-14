import sys 
input = sys.stdin.readline 
n = int(input())

dp = [0 for _ in range(n)]
if n==1:
	print(0)
elif n == 2:
	print(1)
elif n == 3:
	print(1)
else:
	dp[1] = 1 # 2일 때
	dp[2] = 1 # 3일 때
	for i in range(3, n):
		first = float('Inf')
		second = float('Inf')
		third = float('Inf')
		if (i+1)%3 == 0: # 3으로 나눠질 때
			first = 1 + dp[(i+1)//3 -1] #3으로 나눈 몫의 연산 최소값
		if (i+1)%2 == 0: #2로 나눠질때
			second = 1 + dp[(i+1)//2 - 1] #2로 나눈 몫의 연산 최소값
		# third : 1로 뺀 수의 연산 최소값
		dp[i] = min(first, second, 1 + dp[i-1])

	print(dp[n-1])