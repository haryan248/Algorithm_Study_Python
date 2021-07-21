import sys
tc = int(sys.stdin.readline())
data = []
plus_mode = [0] * 4001
minus_mode = [0] * 4000
for i in range(tc):
    a = int(sys.stdin.readline())
    data.append(a)

data.sort()
# 산술평균
print(round(sum(data)/len(data)))


# 중앙값
print(data[len(data)//2])

# 최빈값
plus_mode = [0] * 4001
minus_mode = [0] * 4000
for i in data:
    if i >= 0:  # 0 ~양수
        plus_mode[i] += 1
    else:  # 음수 -1 -2 ..
        minus_mode[abs(i)-1] += 1

maxcount = max(max(plus_mode), max(minus_mode))
if minus_mode.count(maxcount) + plus_mode.count(maxcount) == 1:
    if minus_mode.count(maxcount) == 1:
        print(-(minus_mode.index(maxcount)+1))
    else:
        print(plus_mode.index(maxcount))
else:
    cnt = 0
    for i in range(len(minus_mode)-1, -1, -1):
        if maxcount == minus_mode[i]:
            cnt += 1
            if cnt == 2:
                print(-(i+1))
                break
    if cnt < 2:
        for i in range(len(plus_mode)):
            if maxcount == plus_mode[i]:
                cnt += 1
                if cnt == 2:
                    print(i)
                    break


# 범위
print(data[len(data)-1]-data[0])
