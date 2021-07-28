import sys
N = sys.stdin.readline()

firstX = int(ord(N[0]))- int(ord('a')) + 1
firstY = int(N[1])
move =[(2, -1),(2,1),(-2,1), (-2,-1),(1, 2),(-1,2),(1, -2), (-1, -2)]

cnt = 0
for i in move:
	tmpX = firstX + i[0]
	tmpY = firstY + i[1]
	if tmpX >=1 and tmpX <= 8  and tmpY >=1 and tmpY <=8:
		cnt +=1

print(cnt) 