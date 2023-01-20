from collections import Counter

t = int(input())

for i in range(t):
    n = int(input())
    score = Counter(map(int, input().split()))
    print(f'#{n} {score.most_common(1)[0][0]}')