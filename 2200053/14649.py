# 신용카드 만들기 1
T = int(input())

for t in range(1, T+1):
    a = [] # 홀수
    b = [] # 짝수
    num = input().split()
    #print(type(num[0])) >>> str
    #print(len(num[:3]))
    for i in range(15):
        if int(len(num[:i+1])) % 2 == 1:
            a.append(int(num[i]))
        elif int(len(num[:i+1])) % 2 == 0:
            b.append(int(num[i]))
    
    # print(sum(a) * 2)
    # print(sum(b))
    # print(10 - (((sum(a) * 2) + sum(b)) % 10))

    if ((sum(a) * 2) + sum(b)) % 10 == 0:
        print(f'#{t} {0}')
    else:
        print(f'#{t} {10 - (((sum(a) * 2) + sum(b)) % 10)}')