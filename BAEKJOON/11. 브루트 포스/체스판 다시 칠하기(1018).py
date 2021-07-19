N, M = map(int, input().split())
chess_list = []
wresult = 64
bresult = 64
for i in range(N):
    chess = input()
    chess_list.append(chess)


def chess(x, y, start, second):
    cnt = 0
    for i in range(8):
        for j in range(8):
            # 짝수 행
            if i % 2 == 0:
                # 짝수 번째 열
                if j % 2 == 0:
                    if chess_list[i + x][j + y] != start:
                        cnt += 1
                else:
                    if chess_list[i + x][j + y] != second:
                        cnt += 1
            # 홀수 행
            else:
                # 짝수 번째 열
                if j % 2 == 0:
                    if chess_list[i + x][j + y] != second:
                        cnt += 1
                else:
                    if chess_list[i + x][j + y] != start:
                        cnt += 1
    return cnt


for i in range(N-7):
    for j in range(M-7):
        # WBWBWBWB로 시작하는 체스판
        wresult = min(wresult, chess(i, j, "W", "B"))
        # BWBWBWBW로 시작하는 체스판
        bresult = min(bresult, chess(i, j, "B", "W"))
print(min(wresult, bresult))
