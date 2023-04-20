# 최빈수 구하기

from collections import Counter

T = int(input())

for i in range(1,T+1):
    test_case = int(input())
    num_list = list(map(int, input().split()))
    num_list = reversed(sorted(num_list)) # 리스트를 정렬한다음 뒤집음

    cnt_num = Counter(num_list).most_common(1) # 가장 많이 나온 숫자를 딕셔녀리에서 뽑아서 저장
    print(f'#{i} {cnt_num[0][0]}')