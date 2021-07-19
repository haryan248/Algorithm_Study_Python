tc = int(input())
for i in range(tc):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = int(((x2-x1)**2 + (y2-y1)**2))
    RdistancePlus = r2 + r1
    RdistanceMinus = r2 - r1 if r2 >= r1 else r1 - r2
    # case 1 : 중점이 같으면서 반지름도 같을 경우
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # case 2-1 : 두 원의 반지름 합보다 중점간 거리가 더 길 때
    elif distance > RdistancePlus**2:
        print(0)
    # case 2-2 : 원 안에 원이 있으나 내접하지 않을 때
    elif distance < RdistanceMinus**2:
        print(0)
    # case 3-1 : 내접할 때
    elif distance == RdistanceMinus**2:
        print(1)
    # case 3-2 : 외접할 때
    elif distance == RdistancePlus**2:
        print(1)
    else:
        print(2)
