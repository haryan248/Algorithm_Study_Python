import sys
tc = int(sys.stdin.readline())
member_list = []
cnt = 0
for i in range(tc):
    age, name = map(str, sys.stdin.readline().strip().split())
    cnt += 1
    member_list.append([int(age), name, cnt])

member_list.sort(key=lambda x: (x[0], x[2]))

for member in member_list:
    print(member[0], member[1])
