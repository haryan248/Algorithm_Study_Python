s = input()
newS = str(s.lower())
alpha = []
for i in range(ord('a'), ord('z')+1):
    alpha.append(newS.count(chr(i)))

if alpha.count(max(alpha)) > 1:
    print("?")
else:
    print(chr(alpha.index(max(alpha))+65))
