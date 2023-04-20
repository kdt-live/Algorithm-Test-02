T = int(input())

for _ in range(T):
    t = int(input())


# with open('input.txt', 'r', encoding='UTF-8') as f:
#     T = int(f.readline())
#     for _ in range(T):
#         t = int(f.readline())
#         li = list(map(int, f.readline().split()))

    score_dict = {}
    for score in list(map(int, input().split())):
        score_dict[score] = score_dict.get(score, 0) + 1
    result = sorted(score_dict.items(), key=lambda x: (x[1],x[0]), reverse=True)
    print(f'#{t} {result[0][0]}')