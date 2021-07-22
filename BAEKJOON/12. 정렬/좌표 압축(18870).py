import sys

tc = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
tmpData = sorted(list(set(data)))
# for i in range(len(tmpData)):
#     compareData.append([tmpData[i], i])

# for i in range(len(data)):
#     for j in range(len(compareData)):
#         if compareData[j][0] == data[i]:
#             sys.stdout.write(str(compareData[j][1]) + " ")
#             break
dic = {tmpData[i]: i for i in range(len(tmpData))}
for i in data:
    print(dic[i], end=' ')
