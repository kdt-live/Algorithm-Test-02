# 신용카드 만들기1
# 10
# 4 5 2 0 0 2 0 0 1 9 0 0 4 0 6  
# 6 9 0 9 7 0 1 9 9 8 6 3 0 8 7
# 5 9 8 7 5 8 7 0 1 7 8 6 7 8 4
# 8 3 4 7 8 0 9 1 0 1 0 3 4 8 0
# 4 9 6 6 3 4 4 9 5 7 0 5 5 0 7
# 2 4 7 1 9 6 1 9 0 0 6 5 3 1 4
# 1 2 3 9 0 9 7 0 3 4 3 6 9 9 8
# 3 2 5 4 0 0 6 6 4 5 0 7 7 2 4
# 8 8 7 6 4 6 2 3 1 3 7 6 8 5 5
# 5 1 0 8 7 6 6 7 4 7 2 9 5 3 5

# 1) 홀수 자리 수 (4 x 2) + (2 x 2) + (0 x 2) + (0 x 2) + (1 x 2) + (0 x 2) + (4 x 2) + (6 x 2)
# 2) 짝수 자리 수 5 + 0 + 2 + 0 + 9 + 0 + 1 
# 3) N을 제외한 1) 과 2)를 더한 합은 51이므로 N의 값은 9입니다.

T = int(input())
a = 0
b = 0
cnt1 = 0
cnt2 = 0
n = 0
for test_case in range(1,T+1):
    numbers = list(map(int,input().split()))
    a = numbers[0::2]
    b = numbers[1::2]
    for i in a:
        c = i*2
        cnt1 += c
    for j in b :    
        cnt2 += j
    cnt = cnt1 + cnt2
if cnt % 10 != 0:
    n = 10 - (cnt % 10)
else:
    n = 0
    print(f'# {test_case} {n}')
      
# T = int(input())
# for i in range(T):
#     numbers = list(map(int, input().split()))
#     A = []
#     A = sum(numbers[0::2])*2
#     B = sum(numbers[1::2])
#     N = 0
#     if A + B + N % 10 == 0:
#         print(f"#{i+1} {N%10}")
#     elif A + B + N % 10 > 0: 
#         N = 10 - ((A + B) % 10)
#         print(f"#{i+1} {N%10}")

    
    
    


