import sys
from typing import AnyStr
N = int(sys.stdin.readline())
startlink = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
select = [0 for x in range(N)]
ans = sys.maxsize


def dfs(idx, cnt):
    global ans
    if cnt == N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                # 골라진 선수는 start팀
                if select[i] and select[j]:
                    # 고른 선수 능력치 더함
                    start += startlink[i][j]
                #안 골라진 선수는 link 팀
                elif not select[i] and not select[j]:
                    link += startlink[i][j]
        # 최소 값 리턴
        ans = min(ans, abs(start - link))

    for i in range(idx, N):
        if select[i] == 0:
            select[i] =1
            # 다음 선수 고름
            dfs(i+1,cnt+1)
            # 선수 고른 후 다시 없앰
            select[i]=0

dfs(0,0)
print(ans)