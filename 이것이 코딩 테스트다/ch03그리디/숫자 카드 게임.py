import sys
N, M = map(int, sys.stdin.readline().split())
num_list = []
result = 0
for i in range(N):
    num = list(map(int, sys.stdin.readline().split()))
    num_list.append(num)
for i in num_list:
    result = max(result, min(i))

print(result)
