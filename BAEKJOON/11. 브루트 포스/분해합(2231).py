# 브루트포스 문제는 단순 무식하게 접근한다.
N = int(input())
print_num = 0
for i in range(1, N+1):
    div_num = list(map(int, str(i)))
    sum_num = i + sum(div_num)
    if(sum_num == N):
        print(print_num)
        break
