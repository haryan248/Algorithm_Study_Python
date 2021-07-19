N = int(input())


def fibonacchi(N):
    if N == 0:
        return 0
    elif N == 1 or N == 2:
        return 1
    else:
        return fibonacchi(N-1) + fibonacchi(N-2)


print(fibonacchi(N))
