num = int(input())


def hannoi(start, to, aux, N):
    if N == 1:
        print("%d %d" % (start, to))
        return

    hannoi(start, aux, to, N-1)
    print("%d %d" % (start, to))
    hannoi(aux, to, start, N-1)


print(2 ** num - 1)
hannoi(1, 3, 2, num)
