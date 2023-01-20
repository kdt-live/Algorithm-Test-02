T = int(input())
number = ['3', '4', '5', '6', '9']

for i in range(1, T+1):
    num = list(input())

    for j in range(len(num)):
        if num[0] in number:
            if len(num) == 16:
                print('1')
        else:
            print('0')
        # elif num[0] not in number:
        #     print(f'#{i} 0')

        