import sys 
input = sys.stdin.readline 
n = int(input())
answer = 0
dp = [[0]*10 for j in range(n)]
# dp[i][j] i자리수에서 j로 끝나는 수에 올 수 있는 경우의 수
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 끝자리가 0 , 9 

# print(dp)
for i in range(1, n):
	for j in range(10):
		if j == 0: # 뒷자리가 0 일때는 1에서 온 것이다.
			dp[i][j] = dp[i-1][j+1]
		elif j == 9: #뒷자리가 9 일땐 8에서 온 것이다.
			dp[i][j] = dp[i-1][j-1]
		else: # 뒷자리가 1~ 8일땐 앞뒤에서 온것
			dp[i][j] =  dp[i-1][j+1] + dp[i-1][j-1]

print(dp)
print(sum(dp[n-1])%1000000000)

