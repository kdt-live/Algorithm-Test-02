#  신용카드 만들기 2

T = int(input())

card_list = [input() for i in range(T)]
for i in range(T):
   card_list[i] = card_list[i].replace('-', '') # -를 빼서 숫자만 남긴다.

for i in range(T):
    if card_list[i][0] not in ['3', '4', '5', '6', '9']: # 숫자로 된 문자열이 34569로 시작하지 않으면
        print(f'#{i+1} 0') # 0을 반환
    elif len(card_list[i]) != 16: # 숫자로 된 문자열이 16글자가 아니면
        print(f'#{i+1} 0') # 0을 반환
    else: # 전부 맞을 시
        print(f'#{i+1} 1') # 1을 반환