T = int(input())
for i in range(T):
  N = int(input())
  arr = list(map(int,input().split()))
  avg = sum(arr)/len(arr)
  cnt=0
  for a in arr:
    if a<=avg:
      cnt+=1
  print(f"#{i+1}",cnt)