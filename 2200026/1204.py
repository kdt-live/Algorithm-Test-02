
score_dic = {}
# 테스트 케이스 수 : 10
T = int(input())
for i in range(1, T+1):  # 문제 번호 1~10
    score = list(map(int, input().split()))
    score = sorted(score)

# 가장 많이 나오는 수 찾기
n = 0
while True:
    if n > 100:
        break
    else:
        print(score.count(n))
        n += 1


# 가장 많이 나오는 수 찾기

# 최빈수가 여러개 일 때 max사용해서 출력
