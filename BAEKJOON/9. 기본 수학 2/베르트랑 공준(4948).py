N = 123456*2+1

seive = [True]*N

seive[1] = False
for i in range(2, int(N**0.5)):
    if(seive[i]):
        for j in range(i**2, N, i):
            seive[j] = False


def count(n):
    count = 0
    for i in range(n+1, 2*n+1):
        if(seive[i]):
            count += 1

    return count


while True:
    num = int(input())
    if(num == 0):
        break
    print(count(num))
