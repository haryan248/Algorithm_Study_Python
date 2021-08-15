import sys
input = sys.stdin.readline
n = int(input()) 
arr = list(map(int, input().split()))
dp = [0] * len(arr)
dp[0] = arr[0]
# dp[i] i번쨰 수까지  최대의 연속합
for i in range(1, len(arr)):
    dp[i] = max(arr[i], dp[i-1] + arr[i])
    print(dp)

print(max(dp))
