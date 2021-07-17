tc = int(input())
for i in range(tc):
    H, W, N = map(int, input().split())
    share = N//H + 1
    rest = N % H

    if rest == 0:
        rest = H
        share -= 1

    if share < 10:
        print("%d0%d" % (rest, share))
    else:
        print("%d%d" % (rest, share))
