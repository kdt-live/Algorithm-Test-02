T = int(input())

for t in range(1, T+1):
    len_dict = {}
    for s in map(int, input().split()):
        len_dict[s] = len_dict.get(s, 0) + 1
    
    for s, cnt in len_dict.items():
        if cnt % 2:
            print(f'#{t} {s}')
            break
    