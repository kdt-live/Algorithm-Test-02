# bdppq
# q => p
# p => q
# b => d
# d => b

T = int(input())
for i in range(T):
  word = input()

  result = ''
  for s in word[::-1]:
    if s == 'p':
      result += 'q'
    if s == 'q':
      result += 'p'
    if s == 'b':
      result += 'd'
    if s == 'd':
      result += 'b'
  print(f'#{i+1} {result}')