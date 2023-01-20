T = int(input())
for i in range(T):
    a, b, c = map(int,input().split())
    if a == b and b == c: print("#{} {}".format(i+1, a))
    elif a == b and b != c: print("#{} {}".format(i+1, c))
    elif b == c and c != a: print("#{} {}".format(i+1, a))
    elif c == a and a != b: print("#{} {}".format(i+1, b))