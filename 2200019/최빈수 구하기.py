from collections import Counter

T = int(input())                                # 테스트 갯수

for i in range(1,T+1):                          # T+1만큼 반복
    n = int(input())                                            
    T_list = list(map(int,input().split()))      # T_list 입력
    T_list_dict = Counter(T_list)
    T_list_cnt_max = []
    for key, values in T_list_dict.items():
        if values == max(T_list_dict.values()):
            T_list_cnt_max.append(key)
    print(f'#{n} {max(T_list_cnt_max)}')