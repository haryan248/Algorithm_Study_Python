import sys

n, m = list(map(int, sys.stdin.readline().split()))
s = []


def dfs():
    if len(s) == m:
        sys.stdout.write(' '.join(map(str, s))+ '\n')
        return

    for i in range(1, n+1):
        s.append(i)
        dfs()
        s.pop()


dfs()
