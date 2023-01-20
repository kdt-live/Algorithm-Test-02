import sys
sys.stdin = open("input4.txt","r")
list1 = []
list2 = []
T = int(input())
for i in range(T):
    a = input()
    for j in a:
        list1.append(j)
    for s in range(0,len(list1)):
        if list1[s] == 'b':
            list1[s] = 'd'
        elif list1[s] == 'd':
            list1[s] = 'b'
        if list1[s] == 'p':
            list1[s] = 'q'
        elif list1[s] == 'q':
            list1[s] = 'p'
    list2.append(list1)
    list1 = []

for k in range(T):
    print("#%s"%(k+1) ,end=" ")
    for w in range(len(list2[k])):        
        print(list2[k].pop(),end="")
    print()

"""
bdppq
qqqqpppbbd
"""
#1 pqqbd
#2 bddqqqpppp