tc = int(input())
number = list(map(int, input().split()))
cnt = 0


def check(num):
    i = 1
    result = True
    if num == 1:
        result = False
    else:
        while i < num-1:
            i += 1
            if (num % i == 0):
                result = False
                break
    return result


for i in range(tc):
    if check(number[i]) == True:
        cnt += 1
print(cnt)
