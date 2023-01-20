T = int(input())
for i in range(T):
    population = int(input())
    income = list(map(int,input().split()))
    average = sum(income) // population; count = 0
    for j in range(population):
        if income[j] <= average: count += 1
    print("#{} {}".format(i+1, count))