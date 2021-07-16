string = list(input())
alphaList = [chr(c) for c in range(ord('a'), ord('z')+1)]
answer = []
for i in alphaList:
    if i in string:
        answer.append(string.index(i))
    else:
        answer.append(-1)

for n in answer:
    print(n, end=" ")
