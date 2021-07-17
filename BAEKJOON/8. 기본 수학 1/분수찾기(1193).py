num = int(input())
count = 1
level = 1
plus = 2

if num == 1:
    print("%d/%d" % (1, 1))
    exit()
else:
    while True:
        count += plus
        level += 1
        if num > count:
            plus += 1
        else:
            break

rank = count-num
if level % 2 == 0:
    print("%d/%d" % (level - rank, (level+1)-(level-rank)))
else:
    print("%d/%d" % ((level+1)-(level-rank), level - rank))