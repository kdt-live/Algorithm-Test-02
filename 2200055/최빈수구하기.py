from collections import Counter
T=int(input())
for i in range (T):
    case=int(input())
    st_score=list(map(int,input().split()))
    cnt_score=Counter(st_score).most_common()
    k=sorted(cnt_score,key=lambda x: (x[1],x[0]),reverse=True)
    print(f'#{case} {k[0][0]}')