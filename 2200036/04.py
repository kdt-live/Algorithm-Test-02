#10804 문자열의 거울상

T = int(input())

for i in range(1, T + 1):
    word = input()
    result = ""
    for j in word:
        if j == "p":
            result += "q"
        if j == "d":
            result += "b"
        if j == "b":
            result += "d"
        if j == "q":
            result += "p"    
    result = result[::-1]
    mirror = ''.join(map(str, result))
    print(f"#{i} {mirror}")