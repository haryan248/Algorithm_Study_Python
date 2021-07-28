import sys
N = int(sys.stdin.readline())

cnt = 0
# 시간 계산
for i in range(N + 1):
	for j in range(60):
		for k in range(60):
			if str(N) in str(i) + str(j) + str(k):
				cnt +=1

print(cnt)
