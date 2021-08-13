import sys 
input = sys.stdin.readline 
n = int(input())
a=[]
maxarr = [0*n for _ in range(n)]
limit1 = [0*n for _ in range(n)] #i번째에 limit가 1일때 최대
limit2 = [0*n for _ in range(n)] #i번째에 limit가 2일때 최대

for i in range(n):
	a.append(int(input()))
if n == 1:
	print(a[0])
	exit()
limit1[0] = a[0]
limit1[1] = a[1]
limit2[1] = a[0] + a[1]
maxarr[0] = a[0]
maxarr[1] = a[0] + a[1]
# 0 ~ n-1 까지
for i in range(2,len(a)):
	limit1[i] = a[i] + max(limit1[i-2], limit2[i-2])
	limit2[i] = a[i] + limit1[i-1]
	maxarr[i] = a[i] + max(limit1[i-1], limit2[i-2], limit1[i-2])

print(maxarr[n-1])