# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for t in range(1, T+1):
    num = str(input())
    # 문자열로 받음
    # 시작이 3,4,5,6,9 확인
    if int(num[0]) in [3, 4, 5, 6, 9]:
        if num not in '-':
            if len(num) == 16:
                print(f'#{t} 1')
            elif len(num) == 19:
                print(f'#{t} 1')
            else:
                print(f'#{t} 0')
        else:
            print(f'#{t} 0')
    else:
        print(f'#{t} 0')

        # 숫자 16개 확인

        # 가능하면 1. 불가능 하면 0 출력
