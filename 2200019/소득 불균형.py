from collections import Counter

T = int(input())

for i in range(1,T+1):
    N = int(input())
    a = list(map(int,input().split()))
    a_avr = (sum(a)/len(a))
    a_dict = Counter(a)
    p_c = 0
    
    for key, value in a_dict.items():
        if key <= a_avr:
            p_c += value
            
    print(f'#{i} {p_c}')