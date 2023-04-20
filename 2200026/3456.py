from collections import Counter

new = []

T = int(input())  # 테스트 케이스 수
for t in range(1, T+1):
    num = list(map(int, input().split()))
    num_dic = Counter(num)
    # print(num_dic)
    # 딕셔너리 정렬 해서 출력...?
    # sorted_dic =

    # 딕셔너리에서 값만 빼서 비교하고
    # 값이 작은 딕셔너리 키만 출력한다
