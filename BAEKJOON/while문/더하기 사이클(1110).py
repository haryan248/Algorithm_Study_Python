inputNum = int(input())
cnt = 0
calNum = inputNum
while True:
    result = calNum // 10 + calNum % 10
    newNum = int(str(calNum % 10) + str(result % 10))
    cnt += 1
    if inputNum == newNum:
        break
    calNum = newNum

print(cnt)
