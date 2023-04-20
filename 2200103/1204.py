for i in range(1, int(input()) + 1):
    N = int(input())  # 테스트케이스 번호
    grades = list(map(int, input().split()))  #점수
    frequency = [0] * 101  #0~100점까지의 빈도를 구하기 위함
    mode = 0  #최빈값
    for grade in grades:
        frequency[grade] += 1 #현재점수의 빈도상승
        if frequency[grade] >= frequency[mode]: mode = grade #현재점수 빈도가가 최빈값 이상이면 최빈수 변경
    print(f"#{i} {mode}")
