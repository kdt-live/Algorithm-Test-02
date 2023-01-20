T = int(input())
for t in range(1, T+1):
    Number = list(map(int, input().split('-')))
    list_Number = list(int, Number)
    if Number[0] not in [3,4,5,6,9]:
        print(0)
    elif len(Number) == 16:
        print(0)
    else:
        print('i')
print(list_Number)