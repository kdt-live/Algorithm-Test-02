# 신용카드 만들기 1

T = int(input())
for i in range(1, T+1):
    t = list(map(int, input().split()))
    total = 0
    
    for j in range(1, 16):
        if j % 2 ==1:
            total += (t[i-1]*2)
            print(j, total, t[i+1])
        else:
            total += t[i-1]
            print(j, total, t[i])
    a = total % 10
    print(total)
    print(a)
    
    if a == 0:
        print(f'#{i}', 0)
    else:
        print(f'#{i} {10-a}')




# T = int(input())
# for i in range(1, T+1):
#     t = list(map(int, input().split()))
#     total = 0
#     for j in t:
#         if j % 2 == 1:
#             total += j*2
#         else:
#             total += j
#     a = total % 10
#     print(total)
#     print(a)
    
#     if a == 0:
#         print(f'#{i}', 0)
#     else:
#         print(f'#{i} {10-a}')
        