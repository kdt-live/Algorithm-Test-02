T = int(input())

for test_case in range(1,T+1):
    s = str(input())

    answer = ''

    for i in s[::-1]:
        if i == 'b':
            answer += 'd'
        elif i == 'd':
            answer += 'b'
        elif i == 'q':
            answer += 'p'

        else:
            answer += 'q'

    print("#%d" %test_case, answer)