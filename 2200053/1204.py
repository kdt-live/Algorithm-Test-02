# 최빈수 구하기
# import sys
# sys.stdin = open("2200053/input.txt", "r")

# T = int(input())

# for t in range(1, T+1):
#     dict_ = {}
#     score = list(map(int, input().split()))

num = 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
cnt = 0
for i in range(len(num)):
    #print(i)
    if num[i] == num[:len(num)]:
        cnt += 1
print(cnt)