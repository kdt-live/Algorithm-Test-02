# 1번 (반복문 다섯빈이 계속 출력됨)
import sys
T = int(sys.stdin.readline())
for test_case in range(1,T+1):
    num = input().split('-')
    num = ''.join(num)
    for i in [3,4,5,6,9]:
        if i == int(num[0]):
            if len(num) == 16:
                print(f'#{test_case} 1')
            else:
                print(f'#{test_case} 0')
                
        else:
            print(f'#{test_case} 0')