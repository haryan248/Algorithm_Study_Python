# import sys
# N = int(sys.stdin.readline())

# cnt = 0
# visit=[[0]*N for i in range(N)] 

# def checkVisit(row, col):
#     for i in range(row): #행
#         # 자기 윗 열에 있으면 
#         if  visit[i][col] == 1:
#             return False
#         for j in range(N): #열
#             # 대각선에 있으면
#             if row - i == abs(col - j) and visit[i][j] == 1:
#                 return False         
#     return True


# def queen(row):
#     global cnt
#     if(row == N):
#         cnt += 1
#         return
#     for i in range(N): # 열
#         col = i
#         if checkVisit(row, col):
#             visit[row][col] = 1 # 체스 두기
#             queen(row + 1)
#             visit[row][i] = 0 # 체스 빼기

# queen(0)
# print(cnt)

# 최적화를 적용한 코드
import sys
def find(r):
    global count
    if r == n:
        # n줄 까지 도달했다면 1가지 경우 추가
        count += 1
        return
    for c in range(n):
        # 대각선 값
        s = r + c # 오른쪽 대각선
        b = r - c # 왼쪽 대각선 
        if col[c] and slash[s] and backSlash[b]:
            col[c] = slash[s] = backSlash[b] = False
            find(r+1)
            col[c] = slash[s] = backSlash[b] = True

n = int(sys.stdin.readline())
col = [True] * n
slash = [True] * (n*2+1) # /
backSlash = [True] * (n*2+1) # \
count = 0
find(0)
print(count)