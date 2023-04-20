# 14649. 신용카드 만들기 1
T = int(input())
for t in range(T):
    input_ = list(map(int, input().split()))
    odd_num = []
    even_num = []
    index = 1
    for i in input_:
        if index%2 == 0:
            even_num.append(i)
        else:
            odd_num.append(2 * i)
        index += 1
    res_sum = sum(even_num) + sum(odd_num)
    res = 10 - int(str(res_sum)[-1])
    res = (str(res)[-1])
    print(f'#{t + 1} {res}')