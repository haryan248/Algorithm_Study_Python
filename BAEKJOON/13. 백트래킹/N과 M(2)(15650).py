import sys

n, m = list(map(int, sys.stdin.readline().split()))
s = []


def dfs(start):
    if len(s) == m:
        sys.stdout.write(' '.join(map(str, s))+ '\n')
        return

    for i in range(start, n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()


dfs(1)
