T = int(input())
for i in range(T):
    S = list(map(str, input().split()))
    P = ""
    R = int(S[0])
    for s in S[1:][0]:
        P = P + s*R
    print(P)
