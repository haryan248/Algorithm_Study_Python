# N = int(input())
# result = N
# cnt = 0
# for i in range(0, N):
#     word = input()
#     checkList = []
#     index = 0
#     for char in word:
#         checkList.append(char)
#         if index >= 1 and index <= len(word)-1 and checkList[index-1] != char:
#             if char in checkList[:index]:
#                 break
#         index += 1

#         if len(checkList) == len(word):
#             cnt += 1
# print(cnt)
N = int(input())
answer = 0

for i in range(N):
    word = input()
    for j in range(len(word)):
        if j != len(word)-1:
            if word[j] == word[j+1]:  # 둘이 같으면 패스
                pass
            elif word[j] in word[j+1:]:  # 있던게 나오면 패스
                print(word[j+1:])
                break
        else:
            answer += 1
print(answer)
