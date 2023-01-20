# 문자열의 거울상

T = int(input())            # 테스트 케이스의 수

for t in range(1, T+1):

    word = input()
    result = ''

    for i in word:
      if i == 'b':         # for문 반복시 b가 나오면 d로 바꿔서 결과값통에 더하고 다음 반복을 실행(d, p, q도 동일하게 반복)
         result += 'd'
         continue
      elif i == 'd':
         result += 'b'
         continue
      elif i == 'p':
         result += 'q' 
         continue
      elif i == 'q':
         result += 'p'

    print(f'#{t} {result[::-1]}')   # 결과값통의 문자열을 역슬라이싱, f스트링 해서 출력 


