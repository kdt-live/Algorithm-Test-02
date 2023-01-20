T = int(input())
for i in range(T):
  numbers = list(map(int, input().split()))

  for n in set(numbers): 
    if numbers.count(n) == 1 or numbers.count(n) == 3:
      print(f'#{i+1} {n}')