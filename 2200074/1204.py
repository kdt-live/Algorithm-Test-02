from collections import Counter

T = int(input())

for test_case in range(1, T + 1):
    case_number = int(input())
    scores = list(map(int, input().split(',')))

    most_scores = Counter(scores).most_common()

    most_score = sorted(most_scores, key= lambda x: x[1], reverse=True)[0]

    print(f'#{test_case} {most_score[0]}')