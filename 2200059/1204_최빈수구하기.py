# import sys
# sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for t in range(1, T+1):
    n = int(input())
    # 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력 고려해서 정렬
    nums = sorted(list(map(int, input().split())), reverse=True)
    dic_nums = {}
    for i in nums:
        dic_nums[i] = dic_nums.get(i, 0)+1

    a = sorted(dic_nums.items(), key=lambda x: x[1], reverse=True)

    print(f'#{t} {a[0][0]}')
