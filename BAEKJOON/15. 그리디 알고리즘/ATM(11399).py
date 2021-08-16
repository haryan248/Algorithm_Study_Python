import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
for i in range(N):
	a[i] = [i+1,a[i]]

a.sort(key = lambda x : x[1])
newList = list(map(list, zip(*a)))
result = 0
for i in range(N):
	result+=sum(newList[1][:i+1])
print(result)