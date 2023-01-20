T = int(input())
for num in range(T):
  test_case = list(map(int, input().split()))
  total = 0
  for i,v in enumerate(test_case):
    if (i+1)%2: # 홀수
      total += v*2
    else:
      total += v

  if total % 10:
    result = 10 - (total % 10)
  else:
    result = 0
  print(f'#{num+1} {result}')