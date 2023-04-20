import sys
input = sys.stdin.readline

test = int(input())

for i in range(test):
    string = input().strip()
    new_sting = ""

    # 거울에 비췄을 때 뒤집힌 문자를 매칭하고 새로 만든 문자열에 추가
    for j in range(len(string)):
        if string[j] == "b":
            new_sting += "d"
        elif string [j] == "d":
            new_sting += "b"
        elif string [j] == "p":
            new_sting += "q"
        else:
            new_sting += "p"
        
    # 거울에 비추면 순서가 뒤집어져서 보이므로 새로 만든 문자열을 거꾸로 출력
    print(f"#{i+1} {new_sting[::-1]}")