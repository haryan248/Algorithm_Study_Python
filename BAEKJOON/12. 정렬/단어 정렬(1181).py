import sys
tc = int(sys.stdin.readline())
words = []
for i in range(tc):
    word = sys.stdin.readline().strip()
    words.append(word)
words = list(set(words))
words.sort(key=lambda x: (len(x), x))
print("\n".join(words))
