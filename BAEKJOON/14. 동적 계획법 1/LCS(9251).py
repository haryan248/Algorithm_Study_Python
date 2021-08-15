import sys
input = sys.stdin.readline
firstString = input()
secondString = input()
length1 = len(firstString) - 1 
length2 = len(secondString) - 1
dp = [[0] * length2 for _ in range(length1)]
# dp[i][j] X, Y 각각의 i, j번째 글자까지의 최장 공통 부분 문자열의 길이
for i in range(1, length1):
    for j in range(1, length2):
        if firstString[i] == secondString[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            
print(dp[-1][-1])