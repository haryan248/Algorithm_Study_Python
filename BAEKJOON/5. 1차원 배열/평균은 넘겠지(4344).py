testcase = int(input())
for i in range(testcase):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]
    count = 0
    for i in nums[1:]:
        if avg < i:
            count += 1
    percent = count/nums[0] * 100
    print("%.3f" % percent + "%")
