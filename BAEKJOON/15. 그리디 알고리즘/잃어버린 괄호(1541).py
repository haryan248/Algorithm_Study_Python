import sys
input = sys.stdin.readline
string =  input().rstrip("\n").split("-")
for i in range(len(string)):
	if "+" in string[i]:
		s = string[i].split("+")
		string[i] = sum(list(map(int, s)))
	else:
		string[i] = int(string[i])
result = string[0]
for i in range(1, len(string)):
	result-=string[i]
print(result)