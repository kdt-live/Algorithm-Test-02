T = int(input())

d = 0

result = []

for t in range(1, T + 1):
    
    a, b, c = map(int, input().split())
    
    if a == b:
        d = c
    elif a == c:
        d = b

    result.append(d)

for i in range(1, T + 1):
    
    print(f"#{i} {result[i-1]}")