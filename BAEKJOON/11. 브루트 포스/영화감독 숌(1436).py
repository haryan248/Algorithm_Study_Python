num = int(input())
cnt = 0
end = "666"
while True:
    cnt += 1
    if end in str(cnt):
        num -= 1
    if num == 0:
        break
print(cnt)
