num = map(int, input())
A = list(map(int, input().split()))
# max = A[0]
# min = A[0]
# for i in A:
#     if min >= i:
#         min = i
#     elif max < i:
#         max = i
print(min(A), max(A))
