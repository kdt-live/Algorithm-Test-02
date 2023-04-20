# import sys
# sys.stdin = open('input.txt', 'r')
T = int(input())
for i in range(T):
    n = int(input())
    math = list(map(int, input().split()))
    math_many = {}
    for j in math:
        if j not in math_many:
            math_many[j] = 1
        else:
            math_many[j] += 1
    math_max = []
    for k, v in math_many.items():
        if math_many[k] == max(math_many.values()):
            math_max.append(k)
    print(f'#{n} {max(math_max)}')