# 문제 4 : 소득 불균형
T = int(input()) # 테스트 케이스 수

for t in range(1, T+1):
    N = int(input()) # 입력 줄 수
    income = list(map(int, input().split()))
    average = sum(income)/N
    cnt = 0

    for c in income:
        if c <= average:
            cnt += 1
    print(f'#{t} {cnt}')    
    