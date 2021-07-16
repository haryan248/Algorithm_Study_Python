def swap(num):
    newS = ""
    for i in num:
        newS = i + newS
    return newS


num1, num2 = input().split()
print(int(swap(num1))
      if int(swap(num1)) >= int(swap(num2)) else int(swap(num2)))
