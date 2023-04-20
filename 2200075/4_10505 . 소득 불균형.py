# 4. 
T = int(input())

for t in range(1,T + 1) :
    N = int(input())
    cnt = 0
    numbers = list(map(int,input().split()))
    for number in numbers :
        if sum(numbers) / len(numbers) >= number :
            cnt +=1
        
    print(f'#{t} {cnt}')
