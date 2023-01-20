# 10505 소득 불균형
T = int(input())
for i in range(T):
  total_person = int(input())

  numbers = list(map(int, input().split()))
  mean = sum(numbers)/total_person
  under_numbers = [num for num in numbers if num <= mean]
  print(f'#{i+1} {len(under_numbers)}')
    