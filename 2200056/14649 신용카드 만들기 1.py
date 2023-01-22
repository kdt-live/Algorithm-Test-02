# 1
T = int(input())

for t in range(1, T+1):
    number_list = list(map(int, input().split())) # 입력값 리스트로 받기
    num_1_list = [0, 2, 4, 6, 8, 10, 12, 14] # 홀수번째 인덱스 값
    num_2_list = [1, 3, 5, 7, 9, 11, 13] #  짝수번째 인덱스 값
    result = 0 # 합계 넣을 곳 0으로 설정

    for num1 in num_1_list: # 홀수 인덱스 값 반복문으로 돌리기
        result += number_list[num1] * 2 # 홀수번째 *2 해주고 result값에 누적해주기

    for num2 in num_2_list: # 짝수 인덱스 값 반복문 돌리기
        result += number_list[num2] # 짝수번째 누적합 해주기

    N = 10 - (result % 10) # N 변수에 합계 나머지 빼주기(그게 10으로 떨어지는 값이 되는 N의 값)
    if N == 10: # 하지만 딱 맞게 떨어졌을 경우
        N = 0 # N은 0으로 설정
  
    print(f"#{t} {N}")


# 2 
T = int(input())

for t in range(1, T+1):
    number_list = list(map(int, input().split()))
    num_1_list = number_list[0::2] # 인덱스 규칙으로 0부터 2칸씩 구해주기
    num_2_list = number_list[1::2] # 1부터 2칸씩 구해주기
    result = 0
    for num1 in num_1_list:
        result += num1 * 2
    for num2 in num_2_list:
        result += num2
    N = 10 - (result % 10)
    if N == 10:
        N = 0
  
    print(f"#{t} {N}")