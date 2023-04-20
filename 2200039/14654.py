import sys
sys.stdin = open("C:\\Users\\USER\\Downloads\\input.txt","r")
T = int(input())
for i in range(T):
    credit_card = input()
    hyphen_cnt = credit_card.count("-")
    if len(credit_card) != 16 + hyphen_cnt: print("#{} {}".format(i+1, 0))
    else:
        if int(credit_card[0]) not in [3,4,5,6,9]: print("#{} {}".format(i+1, 0))
        else: print("#{} {}".format(i+1, 1))