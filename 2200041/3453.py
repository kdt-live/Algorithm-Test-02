#3456
# T, 변 3개, 구할 변
# for.. if 변 1개.count = 홀(3=정사각형, 1=직사각형)/짝(직사각형 = 1개인 변을 찾자)

T = int(input())
N = 0

for t in range(1, T+1):
    square = list(map(int, input().split()))
    for n in square:
        if square.count(n) % 2 == 1:
            N = n
            break
    print(f'#{t} {N}')

