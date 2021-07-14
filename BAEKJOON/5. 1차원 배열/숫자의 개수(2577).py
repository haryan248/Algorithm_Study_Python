numbers = []
for i in range(3):
    i = int(input())
    numbers.append(i)

multi = numbers[0]*numbers[1]*numbers[2]
for i in range(10):
    print(str(multi).count(str(i)))
