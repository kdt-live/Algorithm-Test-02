import sys
sys.stdin = open("input5.txt","r")
T = int(input())
list1 = []
check = 0
check1 = 0
check2 = 0
for i in range(T):
    a = list(map(int,input().split()))
    check = (a[0]+a[2]+a[4]+a[6]+a[8]+a[10]+a[12]+a[14])*2
    check += a[1]+a[3]+a[5]+a[7]+a[9]+a[11]+a[13]
    check1 = check%10
    check2 = 10-check1
    if check2 == 10:
        list1.append(0)
    else:        
        list1.append(check2)
    check = 0
    check1 = 0
    check2 = 0
for j in range(T):
    print("#%s %s"%((j+1),list1[j]))