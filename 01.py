from collections import Counter

T = int(input())

for t in range(1, T+1):
    case_num = int(input())
    # test = map(int, sys.stdin.readline().split())
    test = map(int, sys.stdin.readline().split())

    print('#'+str(case_num), Counter(test).most_common(1)[0][0])