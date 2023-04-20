T = int(input())

for t in range(1, T+1):
    t_input = input().strip().replace('-','')
    if t_input[0] not in ['3','4','5','6','9']:
        t_result = 0
    else:
        if len(t_input) == 16:
            t_result = 1
        else:
            t_result = 0

    print(f'#{t} {t_result}')