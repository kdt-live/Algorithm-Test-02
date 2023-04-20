T = int(input())

for t in range(1, T+1) :
    num_li = list(map(int, input().split()))
    summ = 0
    # print(num_li)

    for i in range(len(num_li)) :
        if i % 2 == 0 : # num_li[짝] -> 실제론 홀수번째 수임
            add = num_li[i] * 2
            summ += add
        else : # 짝수번째 수
            summ += num_li[i]
    re = summ % 10   # 51 %10 -> re = 1
    N = 10 - re     # 10 - 1 -> N = 9
    # 위의 식대로 하면 re가 0일 때 N이 10이 나옴
    # if문으로 N == 10 따로 지정
    if N == 10 : 
        print(f'#{t} 0')
    else :       
        print(f'#{t} {N}')       