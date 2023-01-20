T = int(input())
for i in range(T):
  abc = list(map(int,input().split()))
  arr = []
  for a in abc:
    if a not in arr:
      arr.append(a)
    else:
      arr.remove(a)
  print(f"#{i+1}",*arr)
