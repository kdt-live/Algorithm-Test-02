t = int(input())
for i in range(t):
    length = list(map(int, input().split()))
    length.sort()

    # 정렬하면 두번째 수는 무조건 겹치는 수라서 두번째 수와 같지 않은 수 찾기
    if length[0] == length[1]:
        print(f'#{i+1} {length[2]}')
    else:
        print(f'#{i+1} {length[0]}')