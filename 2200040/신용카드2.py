import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
num = ['3', '4', '5', '6', '9']

for t in range(1, T+1):
    number = input()
    # print(number[0])
    if number[0] in num: # 앞 자리 확인
        if len(number) == 16:  # 길이 확인
            if '-' not in number: # - 문자확인
                print(f"#{t} 1")
        elif '-' in number:
            if len(number) == 19:
                print(f"#{t} 1")
        else:
            print(f"#{t} 0")
    else:
        print(f"#{t} 0")








    # if number[0] not in num:
    #     print(f"{t} 1")
    # else:
    #     if '-' in number:
    #         if len(number) == 20:
    #             print(f"#{t} 0")
    #         else:
    #             print(f"{t} 1")
    #     else:
    #         print(f"#{t} 0")
# 카드 번호는 3, 4, 5, 6, 9 로 시작
# 카드 번호에 -가 들어갈 수 있으며 -를 제외한 숫자는 16개
# 앞자리를 확인하는 조건
# 숫자열의 길이16개 대신 -는 제외하고 숫자를 세기
