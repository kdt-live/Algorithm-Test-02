# 14649. 신용카드 만들기 1
T = int(input())
for t in range(T):
    input_ = list(map(int, input().split()))
    test = input_[-1]
    del input_[-1]
    odd = []
    even = []
    cnt = 0
    for i in input_:
        cnt +=1
        if cnt%2 == 1:
            odd.append(i)
        else:
            even.append(i)
    M = 2* sum(odd) +  sum(even)
    M = str(M)
    N = 10 - int(M[-1])
    N = str(list(N[-1]))
    print(f'#{t+1} {N}')