N = int(input())

for i in range(1,N+1):

    numbers = list(map(int,input().split()))

    numbers.sort()

    if numbers[0] != numbers[1]:
        print("#{} {}".format(i,numbers[0]))

    else:
        print("#{} {}".format(i,numbers[2]))