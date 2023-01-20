#14649
# T = [15 int], [홀](초기화),  [짝](초기화), add,  N
# 15 int의 홀 짝을 나누고 각 리스트에 묶는다(for len() in..: if % 2 == 0:)
# 홀에 짝의 합을 더해
# 나온 값이 10의 단위가 아니면 알맞는 N을 구한다
T = int(input())
add= 0 
N = 0

for t in range(1, T+1):
    odd = []
    even = []
    card = list(map(int, input().split()))    
    
    for i in range(1, 16):

        if len(card[0:i]) % 2 == 1:
            odd.append(card[i-1])
        else:
            even.append(card[i-1])

    add = sum(odd * 2) + sum(even)

    if add % 10 != 0:
        N = 10 - add % 10
    else:
        N = 0
    print(f'#{t} {N}')
