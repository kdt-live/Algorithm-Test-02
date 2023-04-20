from collections import Counter

t = int(input())

for i in range(t):
    side = Counter(map(int, input().split())).most_common()
    print(f'#{i + 1} {side[-1][0]}')