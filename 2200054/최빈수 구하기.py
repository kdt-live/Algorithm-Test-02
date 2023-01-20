import sys
input = sys.stdin.readline

TC = int(input())

for i in range(TC):
    tcnum = int(input())
    numbers = list(map(int, input().split()))
    result = {}
    maxnum = 0
    answer = []
    for i in range(len(numbers)):
        if numbers[i] not in result:
            result[numbers[i]] = 1
        if numbers[i] in result:
            result[numbers[i]] += 1
    result = sorted(result.items(), key=lambda x: x[1])
    for i in range(len(result)):
        if result[i][1] > maxnum:
            maxnum = result[i][1]
    for i in range(len(result)):
        if result[i][1] == maxnum:
            answer.append(result[i][0])
    answer = sorted(answer)
    print(f'#{tcnum} {answer[len(answer) - 1]}')       


