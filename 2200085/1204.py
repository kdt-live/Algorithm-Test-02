import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range (T):
    score_dict = {}
    max_freq_scores = []

    test_case = int(input())
    scores = list(map(int, input().split()))

    for score in scores:
        if score not in score_dict:
            score_dict[score] = 1
        else:
            score_dict[score] += 1
    
    freq = max(list(score_dict.values()))

    for score in scores:
        if score_dict[score] == freq:
            max_freq_scores.append(score)

    max_freq = max(max_freq_scores)

    print(f'#{test_case} {max_freq}')