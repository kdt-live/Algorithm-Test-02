def card(n):
    flag = True
    if n[0] not in ('34569'):
        flag = False
    else:
        cnt = 0
        for element in n:
            if element.isdigit():
                cnt += 1
        if cnt != 16:
            flag = False

    if flag:
        return 1
    else:
        return 0

t = int(input())

for i in range(t):
    number = input()
    print(f'#{i + 1} {card(number)}')