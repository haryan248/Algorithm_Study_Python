def self_num(num):
    constructor = num
    for i in str(num):
        constructor += int(i)
    return constructor


generated_num = set()
natural = set(range(1, 10001))

for i in range(1, 10001):
    generated_num.add(self_num(i))

self_num = sorted(natural - generated_num)

for i in self_num:
    print(i)
