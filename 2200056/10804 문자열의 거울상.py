T = int(input())
for t in range(1, T+1):
    string = input()
    a = len(string)
    print(a)
    if a % 2 == 0:
        for i in range(0, a/2+1):
            j = (a-i)-1
            string[i], string[j] = string[j], string[i]
    else:
        for i in range(0, a//2+1):
            j = (a-i)-1
            string[i], string[j] = string[j], string[i]
    print(string)  #....왜 오류나지ㅠㅠ