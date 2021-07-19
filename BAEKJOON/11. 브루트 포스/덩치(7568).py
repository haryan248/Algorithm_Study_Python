tc = int(input())
kg_list = []
cm_list = []
rank = [0] * tc
for i in range(tc):
    kg, cm = map(int, input().split())
    kg_list.append(kg)
    cm_list.append(cm)

for i in range(tc):
    for j in range(tc):
        if i != j:
            if kg_list[i] > kg_list[j] and cm_list[i] > cm_list[j]:
                rank[i] += 1
            elif kg_list[i] >= kg_list[j] and cm_list[i] <= cm_list[j] or kg_list[i] <= kg_list[j] and cm_list[i] >= cm_list[j]:
                rank[i] += 1

for i in rank:
    print(tc - i, end=" ")
