# 신용 카드를 만들려면 아래 두 가지의 조건을 모두 만족해야 한다.

# 1. 카드 번호는 3, 4, 5, 6, 9 로 시작해야 한다.
# 2. 카드 번호에 "-"이 들어갈 수 있으며 "-" 를 제외한 숫자의 개수는 16개이다.
# EX) 6471-6836-9525-5276
# EX) 3029192045012901

# 카드 번호가 주어졌을 때 해당 번호로 신용카드를 만들 수 있는지 판별하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

TC = int(input())
for t in range(1, TC+1):
    string = input().rstrip()
    # if string[0] in ['3','4','5','6','9']:
    if string[0] in '34569':
        if(len(string)) > int(15):
            print(f'#{t} 1')
        else:
            print(f'#{t} 0')
    else:
        print(f'#{t} 0')