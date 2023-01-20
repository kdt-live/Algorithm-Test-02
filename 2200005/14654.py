l = ['3','4','5','6','9']
a =  int(input())
for i in range(a):
    num = input()
    num = num.replace('-','')
    if (num[0] in l)and len(num)==16:
        print(f'#{i+1} 1')
    else:
        print(f'#{i+1} 0')