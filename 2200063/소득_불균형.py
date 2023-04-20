# n명의 사람의 소득이 주어졌을 때 이 중 평균 이하의 소득을 가진 사람들의 수를 출력

# 입력: 첫 줄에 테스트 케이스 T입력
# 이후 T개의 테스트 케이스에 대해 각각 두줄로 입력
# 첫 번째 줄에는 정수 개수 N이 주어지며 두 번째 줄에는 각 사람의 소득을 뜻하는 N개의 양의 정수가 주어진다

# 출력 : 각 테스트 케이스마다 한 줄씩 평균 이하의 소득을 가진 사람들의 수를 출력한다.

# 접근 : 1) 소득평균값 = 소득총합 / 사람수 2) 소득평균값을 각 소득에 비교하여 평균값보다 낮을시 카운트 1씩 추가

T = int(input())

for t in range(T):
    P = int(input())
    N = list(map(int, input().split()))
    average = sum(N) / P
    cnt = 0

    for n in N:
        if n <= average:
            cnt += 1

    print(f'#{t+1} {cnt}')