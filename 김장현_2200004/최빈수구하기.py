
t = int(input())

for i in range(t):
    test_number = int(input())
    a = list(map(int, input().split()))
    score_dict = {}
    score_list = []
    for j in a:
        if j not in score_dict:
            score_dict[j] = 1
        else:
            score_dict[j] += 1

    often = max(score_dict.values())
    for key, value in score_dict.items():
        if value == often:
            score_list.append(key)
    if len(score_list) == 1:
        print(f'#{test_number}', score_list[0])
    else:
        print(f'#{test_number}', max(score_list))
