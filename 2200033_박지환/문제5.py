# 직사각형 길이 찾기

T = int(input())
len_list = [list(map(int, input().split())) for i in range(T)]

for i in range(T):
    tmp = 0
    for j in len_list[i]: # j와 j-1을 xor 연산 시킴
        j = tmp ^ j     
        tmp = j

    print(f'#{i+1} {tmp}')