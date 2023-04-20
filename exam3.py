import sys
sys.stdin = open("input3.txt","r")

T = int(input())
list1=[]
count = 0
for i in range(T):
    people = int(input())
    income = list(map(int,input().split()))
    average = sum(income)/people
    for j in income:
        if j <= average:
            count += 1
    list1.append(count)
    count = 0
for k in range(1,T+1):
    print("#%s %s"%(k,list1[k-1]))