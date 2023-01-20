from collections import Counter
t = int(input())
for _ in range(1, t+1):

    tc_num = int(input())
    score = list(map(int, input().split()))

    cnt = Counter(score).most_common()
    max_num = max(cnt, key= lambda x:x[1])[1]
    print(f'#{tc_num} {max(cnt, key= lambda x : x == max_num)[0]}')