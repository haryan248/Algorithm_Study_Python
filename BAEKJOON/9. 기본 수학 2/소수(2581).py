M = int(input())
N = int(input())

arry = []
for i in range(M, N+1, 1):
    if i != 1:
        check = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = False
                break
        if check:
            arry.append(i)

if len(arry) != 0:
    print(sum(arry))
    print(min(arry))
else:
    print(-1)
