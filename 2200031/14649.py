T = int(input())

for i in range(1, T+1):
    num_hol = []
    num_jjak = []
    hol_sum = 0
    jjak_sum = 0
    N = 0
    result = 0

    num = list(map(int, input().split()))
    
    for j in range(len(num)):
        if j%2 == 0:
            num_hol.append(num[j])
            hol_sum = sum(num_hol*2)
        else:
            num_jjak.append(num[j])
            jjak_sum = sum(num_jjak)

    hap = hol_sum + jjak_sum
        

    while(True):
        result = hap + N
        if result % 10 != 0:
            N += 1
        else:
            break

    print(f'#{i} {N}')




    


