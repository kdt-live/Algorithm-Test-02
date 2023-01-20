#10804
# T, 문자열, 리스트(초기화)
# 문자열을 [::-1]
# replace를 쓰면 계속 변경이 될것 같으니 for로 따로 봐야 할 것같은 느낌
# for에 if문을 넣어서 알맞게 변경

T = int(input())
for t in range(1, T+1):
    s_list = []
    
    S = input()[::-1]   
    for s in S:
        if s == "b":
            s_list.append("d")
        elif s == "d":
            s_list.append("b")
        elif s == "p":
            s_list.append("q")
        else:
            s_list.append("p")

    print(f'#{t} ', end = "")
    print(*s_list, sep = "")