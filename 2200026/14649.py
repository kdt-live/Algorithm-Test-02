
odd = []
even = []
n = [0, 2, 4, 6, 8, 10, 12, 14]
n_even = [1, 3, 5, 7, 9, 11, 13]

T = int(input())  # 테스트 케이스 수
for t in range(1, T + 1):
    card = list(map(int, input().split()))
    # 4 5 2 0 0 2 0 0 1 9 0 0 4 0 6
    # 4 9 6 6 3 4 4 9 5 7 0 5 5 0 7

    # 자리가 홀수면 숫자마다 2를 곱해서 더함
    for i in n:
        odd.append(card[i]*2)
    # print(odd) [8, 4, 0, 0, 2, 0, 8, 12]
    odd_sum = sum(odd)
    # 자리가 짝수면 숫자 다 더하기
    for i in n_even:
        even.append(card[i])
    # print(even) [5, 0, 2, 0, 9, 0, 0]
    even_sum = sum(even)

    # 짝수 홀수 나온결과로 다 더하고
    total = odd_sum + even_sum
    # (홀 + 짝 + N) % 10 == 0
    if total % 10 == 0:
        print(f'#{t} 0')
        odd.clear()
        even.clear()
    else:
        num = total % 10
        N = 10 - num
        print(f'#{t} {N}')
        even.clear()
        odd.clear()
