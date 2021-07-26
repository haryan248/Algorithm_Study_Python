import sys

n, m = list(map(int, sys.stdin.readline().split()))

s = []

def dfs(x):
    if len(s) == m:
        sys.stdout.write(' '.join(map(str, s))+ '\n')
        return
    
    for i in range(x, n+1): # 1 ~ N까지
            s.append(i)
            dfs(i)
            s.pop()

dfs(1)