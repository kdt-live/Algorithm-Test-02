T = int(input())
for i in range(T):
  sum = 0
  arr = list(map(int,input().split()))
  for idx in range(len(arr)):
    if (idx+1)%2==1:
      sum+=arr[idx]*2
    else:
      sum+=arr[idx]
  for N in range(0,10):
    if (sum+N)%10==0:
      print(f"#{i+1}",N)