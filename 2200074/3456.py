T = int(input())

for test_case in range(1, T + 1):
    lines = list(map(int, input().split()))
    lines.sort()
    result = lines[-1] if lines[0] == lines[1] else lines[0]

    print(f'#{test_case} {result}')