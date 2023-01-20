T = int(input())

for t in range(1, T+1):
    nums = input().split()

    for n in nums:
        if nums.count(n) > 2 or nums.count(n) == 1:
            the_line = n
            break

    print('#', t, ' ', the_line, sep='')