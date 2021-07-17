numbers = (input().split())
A = int(numbers[0])  # 고정 비용
B = int(numbers[1])  # 가변 비용
C = int(numbers[2])  # 판매가격

if B >= C:
    print(-1)
else:
    i = A//(C-B) + 1
    print(i)
# print(i)
# print((10 * 210000001) - (2100000000 + (9 * 210000001)))
# if B > C:
#     print(-1)
# else:
#     while True:
#         i += 1
#         if (C * i) - (A + (B * i)) >= 0:
#             break
#     print(i)
