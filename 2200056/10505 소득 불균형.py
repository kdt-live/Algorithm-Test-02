T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split())) # 인풋값 리스트에 저장
    num_list_avg = sum(num_list) / len(num_list) # 리스트 평균값 구하기
    result_list = []
    for num in num_list:
        if num <= num_list_avg: # num_list의 요소들 중에 평균값과 같거나 작은 경우만
            result_list.append(num) # result_list에 추가하기
    result = len(result_list) # result_list 요소들 구하기
    print(f"#{t} {result}")