# 어느 고등학교에서 실시한 1000명의 수학 성적을 토대로 통계자료를 만든다
# 최빈수를 이용하여 학생들의 평균 수준을 짐작하는데 여기서 최빈수란 특정 자료에서 가장 여러번 나타나는 값을 의미한다.
# 최빈수 출력 프로그램

# 학생수 1000명, 각 학생의 점수는 0점이상 100점 이하의 값

# 입력 첫줄 테스트 케이스 수 T가 주어진다.
# 각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.
# 출력 : # 부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

import sys
sys.stdin = open('input.txt', mode='r', encoding='UTF-8')
input = sys.stdin.readline
T = int(input())
for n in range(T):
    exam = {}
    t = int(input())
    score = input().split()
    for i in score:
        if i not in exam:
            exam[i] = 1
        else:
            exam[i] += 1
    # exam = sorted(exam.values(), reverse=True)
    
    exam = sorted(exam.items(), key= lambda x: -x[1])
        

    print(f'#{t} {exam[0][0]}')
    
