import sys
input = sys.stdin.readline

# 첫 번째 테스트 케이스 수를 저장하는 변수
test = int(input())

for i in range(test):
    # 두 번째 테스트 케이스 수를 저장하는 변수
    num = int(input())
    # 평균 이하인 수를 저장하는 변수
    cnt = 0

    # num개의 수를 입력받아 리스트로 저장
    income = list(map(int, input().split()))

    # 리스트의 평균을 계산하여 변수에 저장
    mean = sum(income) // num

    # 리스트를 순회하면서 평균 이하인 수를 체크
    for j in range(num):
        if income[j] <= mean:
            cnt += 1

    print(f"#{i+1} {cnt}")