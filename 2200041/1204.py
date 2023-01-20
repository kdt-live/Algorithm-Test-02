#1204
# T, dict, 점수
# 점수를 받고 if 같은수가 없으면 딕셔너리에 점수 : 1 있으면 +1
# valus가 제일 큰 수는?

T = int(input())

for t in range(1, T+1):
    num = int(input())
    score_dict = {}
    scores = list(map(int, input().split()))
    
    for score in scores:
        if score not in score_dict:
            score_dict[score] = 1
        else:
            score_dict[score] += 1

    many = max(score_dict.items(), key = lambda x: x[1])
    # 더 쉽고 좋은 방법이 있을까? max(score_dict.value())가 안됐다.
    # 어제 비슷한 방식으로 풀었던 것 같은데 왜일까?
    
    print(f'#{t} {many[0]}')