#직사각형 길이 찾기
T = int(input())
for i in range(1,T+1):
    
    num_list = list(map(int,input().split()))
    for j in num_list:
        if num_list.count(j) == 1 or num_list.count(j) == 3:
            answer = j
    print(f'#{i} {answer}')