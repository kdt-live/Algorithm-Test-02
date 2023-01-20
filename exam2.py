import sys
sys.stdin = open("input2.txt","r")
T = int(input())
list1 = []
for i in range(T):
    a,b,c = map(int,input().split())
    if a == b:
        list1.append(c)
    elif b == c:
        list1.append(a)
    elif c == a:
        list1.append(b)
for j in range(1,T+1):
    print("#%s %s"%(j,list1[j-1]))