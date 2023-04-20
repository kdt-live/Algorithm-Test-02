import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    card = input().strip()
    is_possible = True # 생성 가능한지를 저장하기 위한 bool 변수
    cnt = 0 # 번호 중에서 숫자 개수를 세기 위한 변수

    # 입력된 카드 번호를 순회하면서 조건에 일치되는지 판단
    for j in range(len(card)):
        # 카드 번호가 0, 1, 2, 7, 8로 시작되면 안되므로 is_possible에 False를 저장하고 for문을 빠져나감
        if card[0] == "0" or card[0] == "1" or card[0] == "2" or card[0] == "7" or card[0] == "8":
            is_possible = False
            break

        # 카드 번호는 자연수와 -로만 이루어져 있으므로 -가 아닌 모든 문자는 숫자라고 볼 수 있음
        # 때문에 -가 아니면 cnt에 1을 더해서 숫자가 모두 몇개인지 판단
        if card[j] != "-":
            cnt += 1
        
    # 숫자가 16개가 아니면 카드를 만들 수 없으므로 is_possible에 False를 저장
    if cnt != 16:
        is_possible = False
    
    print(f"#{i+1} {int(is_possible)}")