def luhn(n):
    result = 0
    
    for i in range(1, 16):
        if i % 2 != 0:
            result += 2 * n[i - 1]
        else:
            result += n[i - 1]
    
    for i in range(10):
        if (result + i) % 10 == 0:
            return i

t = int(input())

for j in range(t):
    number = list(map(int, input().split()))
    print(f'#{j + 1} {luhn(number)}')
