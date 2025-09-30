
nums = list(map(int, input().split()))

for n in nums:
    s = str(n) + "10"
    big_num = int(s * 4)
    root = big_num ** (1/10)
    print(root)
