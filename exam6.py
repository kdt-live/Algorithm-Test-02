import sys
sys.stdin = open("input6.txt","r")
list1 = []
T = int(input())
for i in range(T):
    a = input()
    a = a.replace('-',"")
    if len(a) == 16:
        if a[0]=='3' or a[0]=='4' or a[0]=='5' or a[0]=='6' or a[0]=='9':
            list1.append(1)
        else:
            list1.append(0)
    else:
        list1.append(0)

for j in range(T):
    print("#%s %s"%((j+1),list1[j]))