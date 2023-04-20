T = int(input())
for i in range(T):
    credit_card = list(map(int,input().split())); sum_odd = 0; sum_even = 0
    for j in range(len(credit_card)):
        if j % 2 == 0: sum_odd += credit_card[j] * 2
        elif j % 2 == 1: sum_even += credit_card[j]
    N = 10 - ((sum_odd + sum_even) % 10)
    if N == 10: N = 0
    print("#{} {}".format(i+1, N))