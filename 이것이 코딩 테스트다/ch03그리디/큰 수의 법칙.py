import sys
N, M, K = map(int, sys.stdin.readline().split())
sum = 0
num = list(map(int, sys.stdin.readline().split()))

if num.count(max(num)) == 2:
    print(max(num)*M)
else:
    first = max(num)
    num.remove(max(num))
    second = max(num)
    while M > 0:
        sum += first * K
        M -= K
        if M == 0:
            break
        sum += second
        M -= 1
        if M == 0:
            break
    print(sum)
