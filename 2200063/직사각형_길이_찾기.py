# 직사각형의 네 변 중에서 세 변의 길이가 주어진다.
# 나머지 한 변의 길이가 얼마인지 출력하는 프로그램 작성
# 세 변의 길이는 상하좌우 어디든 될 수 있으므로 그 순서는 중요하지 않다.

# 입력 : 첫번째 줄 테스트 케이스 T, 각 테스트 케이스에서 a, b, c 입력

# 출력: 각 테스트 케이스마다 나머지 한 변의 길이를 출력한다.

T = int(input())

for t in range(T):
    a, b, c = map(int, input().split())
    if a == b and b == c:
        print(f'#{t+1} {a}')

    elif a == b and a != c:
        print(f'#{t+1} {c}')

    elif a != b and a == c:
        print(f'#{t+1} {b}')
    
    elif a != b and b == c:
        print(f'#{t+1} {a}')