import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    # 입력되는 수는 공백을 기준으로 나눌 수 있는 정수들이기 때문에 리스트에 저장
    numbers = list(map(int, input().split()))
    # 모든 숫자들의 총 합을 저장할 변수
    total = 0

    for j in range(15):
        # 인덱스는 0부터지만 순서는 1부터 시작이므로 인덱스에 1을 더해준 상태로 판별
        if (j+1) % 2 == 0:
            total += numbers[j]
        else:
            total += numbers[j] * 2
    
    # 10 - (total % 10)만 하면 0이 나올 수 없으므로 다시 10으로 나눈 나머지를 출력
    print(f"#{i+1} {(10 - (total % 10)) % 10}")