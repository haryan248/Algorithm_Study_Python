import sys
N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
operate = list(map(int, sys.stdin.readline().split()))
minAns = float('Inf')
maxAns = float('-Inf')
def dfs(index,res):
    global minAns
    global maxAns
    # 계산의 끝에 도달했을 때 최댓값과 최솟값이 될 수 있는지 판단한다.
    if index==N-1:
        maxAns = max(res, maxAns)
        minAns = min(res, minAns)
        return res
    # 백트래킹 DFS로 순회
    for i in range(4):
        temp = res
        if operate[i]==0:
            continue
        if i==0:
	        res+=num[index+1]
        elif i==1:
            res-=num[index+1]
        elif i==2:
            res*=num[index+1]
        else:
            if res<0:
                res = abs(res)//num[index+1]*-1
            else:
                res //=num[index+1]

        operate[i] -= 1
        dfs(index+1,res)
        operate[i] += 1
        res = temp

dfs(0,num[0])
print(str(maxAns) + "\n" + str(minAns))
