T = int(input())
  
for i in range(T):
  case = int(input())
  cnt = [0 for _ in range(101)]
  arr = list(map(int,input().split()))
  for num in arr:
    cnt[num]+=1
  cnt2 = []
  for i in range(101):
    cnt2.append((i,cnt[i]))
  cnt2.sort(key=lambda x:(x[1],x[0]),reverse=True)
  #print(cnt2)
  print(f"#{case}",cnt2[0][0])