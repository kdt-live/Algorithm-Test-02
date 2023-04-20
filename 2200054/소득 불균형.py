import sys
input = sys.stdin.readline

TC = int(input())
for t in range(1, TC+1):
    N = int(input()); inputnumbers = list(map(int, input().split())); numbers = []

    for i in range(N): # 숫자를 N개 초과해서 입력햇을때를 대비한 리스트 재 설정.
        numbers.append(inputnumbers[i])
    avr = sum(numbers) // len(numbers)
    cnt = 0
    for i in numbers:
        if i <= avr:
            cnt += 1
    print(f'#{t} {cnt}')

