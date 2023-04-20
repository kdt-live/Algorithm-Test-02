# 1204 최빈수 구하기

T = int(input())
for i in range(T):
  test_case = int(input())
  numbers = list(map(int, input().split()))
  score_dict = {}
  for num in range(101):
    score_dict[num] = numbers.count(num)


  common_score_list = [score for score,count in score_dict.items() if max(score_dict.values()) == count]
  common_score = max(common_score_list)

  print(f'#{i+1} {common_score}')

