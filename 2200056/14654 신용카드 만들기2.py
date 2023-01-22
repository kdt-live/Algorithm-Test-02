T = int(input())
num_list = ["3", "4", "5", "6", "9"] # 카드번호 앞자리 조건 리스트 만들기
for t in range(1, T+1):
    credit_card = input()
    
    if len(credit_card) == 16: # 카드번호가 16자리인 경우 카드번호 조건
        if credit_card[0] in num_list: # 그 중에서 앞자리 조건 리스트를 만족 시킬 경우
            print(f"#{t} 1")
        else:
            print(f"#{t} 0")

    elif len(credit_card) > 16: # 16자리 이상인 경우 (-가 있는 경우)
        for num in credit_card:
            if num == "-": # 카드번호에 -가 있는 경우
                new_credit_card = credit_card.replace(num, "") # -를 공백으로 바꾸기
        if len(new_credit_card) == 16 and credit_card[0] in num_list: # 공백으로 바꾼 후 자리가 16자리 이면서 앞자리 카드번호 조건을 만족 할 경우
            print(f"#{t} 1")
        else:
            print(f"#{t} 0")
    else:
        print(f"#{t} 0")