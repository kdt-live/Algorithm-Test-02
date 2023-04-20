import sys
sys.stdin = open("input (3).txt", "r")

# T = int(input())
# for t in range(1, T + 1):
#     case = int(input())
#     nums = list(map(int, input().split()))
#     cnt_list = []
#     for i in range(101):
#         cnt = nums.count(i)
#         cnt_list.append(cnt)
#     print(cnt_list.index(max(cnt_list)))
#     print(f'#{case} {cnt_list.index(max(cnt_list))}')

# 제~발 문제를 잘 읽자.

T = int(input())
for t in range(1, T + 1):
    case = int(input())
    nums = list(map(int, input().split()))
    cnt_list = []
    for i in range(100, -1, -1):    # index는 제일 먼저 나오는 것부터 구한다. 그러면 작은 수를 찾게 된다. 그러니 뒤집자.
        cnt = nums.count(i)
        cnt_list.append(cnt)
    print(f'#{case} {100 - cnt_list.index(max(cnt_list))}')
    
