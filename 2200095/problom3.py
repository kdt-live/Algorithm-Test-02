# 10505. 소득 불균형
T = int(input())
cnt = 1
for t in range(T):
    test_case = int(input())
    input_list = list(map(int,input().split()))
    res_list = []
    for i in input_list:
        avg = sum(input_list)/len(input_list)
        if i <= avg:
            res_list.append(i)
            
    print(f'#{cnt}',len(res_list))
    cnt += 1