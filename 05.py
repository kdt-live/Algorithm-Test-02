# 소득 불균형

T= int(input())
for t in range(1,T+1):
    people = int(input())
    money = map(int,input().split())
    avg = sum(money) // people
    count = 0

    for i in money:
        if i <= avg:
            count +=1
    print(f'#{t} {count}')

# 맞는지는 모르겠어요 ㅎ ㅠ 시간이 없어서 값을 입력 못해봐ㅏㅆ어요 