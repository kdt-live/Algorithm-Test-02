T = int(input()) ## 못품

for i in range(1, T+1):
    num_list = []
    hap = 0

    num = int(input())
    number = list(map(int, input().split()))

    for j in range(len(number)):
        # if number[j] not in num_list:
        #     num_list.append(number[j])
        # else:
        #     hap += 1
        number_count = number.count(j)
            

