import sys
N = int(sys.stdin.readline())

command = list(sys.stdin.readline().split())
now = [1, 1]
for i in range(len(command)):
    if command[i] == "R" and now[1] < N:
        now[1] += 1
    elif command[i] == "L" and now[1] > 1:
        now[1] -= 1
    elif command[i] == "U" and now[0] > 1:
        now[0] -= 1
    elif command[i] == "D" and now[0] < N:
        now[0] += 1
for i in now:
    print(i, end=" ")
