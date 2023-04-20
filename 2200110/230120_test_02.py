T = int(input())
for t in range(1, T+1):
    card_num = list(map(int, input().split()))

    even_num = 0
    odd_num = 0

    for i in range(len(card_num)):
        if i % 2 == 0:
            odd_num += card_num[i]
        else:
            even_num += card_num[i]

    if (odd_num * 2 + even_num) % 10 == 0:
        N = 0
    else:
        N = 10 - (odd_num * 2 + even_num) % 10
    print(f'#{t} {N}')
