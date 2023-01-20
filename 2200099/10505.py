T = int(input())
for t in range(1,T+1):
    case = int(input())
    pay = list(map(int, input().split()))
    tmp_pay = sum(pay)//case
    result = 0
    for i in pay:
        if tmp_pay >= i:
            result += 1
    print(f'#{t} {result}')
