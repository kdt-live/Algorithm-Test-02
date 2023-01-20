T = int(input())
 
for i in range(T):
    case_num = int(input())
    score = list(map(int, input().split()))

    list_score = [0 for i in range(101)]
    common = 0
    for j in score:
        list_score[j] += 1
        if list_score[j] >= list_score[common]:
            common = j
 
    print(f'#{case_num} {common}')