# # 소득 불균형
T = int(input())
for test_case in range(T):
    N = int(input())       
    income = list(map(int,input().split()))
    average = (sum(income)/len(income))
    cnt = 0
    for i in income:
        if i <= income:
            cnt += 1

    print(f'# {test_case} {cnt}')

T = int(input())
for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    A = (sum(numbers)/len(numbers))
    count =0
    for j in numbers:
        if j <= A:
            count += 1
    print(f"#{i+1} {count}")

