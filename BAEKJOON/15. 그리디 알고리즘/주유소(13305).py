# import sys
# input = sys.stdin.readline
# N = int(input())
# distance = list(map(int,input().split()))
# liter = list(map(int,input().split()))
# min_liter = liter.index(min(liter[:len(liter)-1]))

# result = 0
# for i in range(N-1):
#     if i == min_liter and i==0:
#         result += sum(distance[min_liter:])*liter[i]
#         break
#     elif liter[i] <= liter[i+1]: #현재 리터값이 다음 리터값보다 작으면
#         if i != min_liter: #현재 리터값이 최소값이 아니면
#             result += sum(distance[:min_liter])*liter[i]
#             # result += sum(distance[min_liter:])*liter[min_liter]
#             break
#         else: # 현재 리터값이 최소값이면
#             result+= sum(distance[i:])*liter[i]
#             break
#     else: #현재 리터값이 다음 리터값보다
#         result += distance[i]*liter[i]
# print(result)
N = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))

minVal = cities[0]
sum = 0
for i in range(N-1):
    print(i)
    if minVal > cities[i]:
        
        minVal = cities[i]
    sum += (minVal * roads[i])
    # print(sum)
    
print(sum)