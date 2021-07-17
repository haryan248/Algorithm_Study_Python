M, N = map(int, input().split())

prime = [True]*(N+1)
prime[0] = False
prime[1] = False
for i in range(2, int(N**0.5)+1):
    if prime[i]:
        for j in range(2*i, len(prime), i):
            prime[j] = False

for n in range(M, N+1):
    if prime[n]:
        print(n)
