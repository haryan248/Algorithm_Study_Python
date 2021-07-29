import sys

N = int(sys.stdin.readline())
nums=[]


for i in range(N):
	nums.append(int(sys.stdin.readline()))
zero = [0 for i in range(max(nums)+1)]
one = [0 for i in range(max(nums)+1)]
zero[0] = 1 # 0번째 0은 1번
zero[1] = 0
one[0] = 0
one[1] = 1

def fibonacci(num):
	if num >= 2:
		for i in range(2, num + 1):
			zero[i]= zero[i-1] + zero[i-2]
			one[i]= one[i-1] + one[i-2]
		print(zero[num], one[num])
	else:
		print(zero[num], one[num])


for num in nums:
	fibonacci(num)
