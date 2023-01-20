from collections import Counter

for t in range(1, int(input())+1):
    n = int(input())
    a = list(map(int, input().split()))
    counter = Counter(a)
    most_num = counter.most_common()[0][0]
    print(f'#{t} {str(most_num)}')