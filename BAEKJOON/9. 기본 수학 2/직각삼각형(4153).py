while True:
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0:
        break
    long = max(A, B, C)
    
    if long == A:
        if B**2 + C**2 == long**2:
            print("right")
        else:
            print("wrong")
    elif long == B:
        if A**2 + C**2 == long**2:
            print("right")
        else:
            print("wrong")
    elif long == C:
        if A**2 + B**2 == long**2:
            print("right")
        else:
            print("wrong")
    
