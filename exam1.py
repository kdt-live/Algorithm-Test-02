import sys
sys.stdin = open("input1.txt","r")
T = int(input())
dic={}
dic1 = {}
record = []
list1=[]
for i in range(T):
    a = input()
    dic[a]=""
    record = list(map(int,input().split()))
    for j in record:
        if j not in dic1:
            dic1[j] = 1
        else:
            dic1[j] += 1

    b = sorted(dic1.values(),reverse=True)
    c = b[0]
    for p in dic1:
        if dic1[p] == c:
            list1.append(p)
            list1.sort(reverse=True)
            p = list1[0]
            dic[a] = p
    dic1 = {}
    record = []
    list1 = []

for q in range(1,T+1):
    print("#%s %s"%(q,dic[str(q)]))