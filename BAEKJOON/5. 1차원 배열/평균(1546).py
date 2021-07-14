testcase = int(input())
sum = 0
number = list(map(int, input().split()))
max = max(number)
for i in range(testcase):
    number[i] = number[i]/max*100
    sum += number[i]
print(sum/testcase)
