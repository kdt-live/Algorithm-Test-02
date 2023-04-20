# 2번 
# 룬공식 구하는 방법 -> 반복되는 홀수자리 마다 2를 곱해서 더함 -> 반복 안에서(번호 리스트를 반복)홀수자리인지 비교하고 2를 곱해서 통(변수)에 집어넣기
# 짝수자리면면 그대로 통에 집어넣기
# 홀수통과 짝수통을 더해서 마지막자리 수 N이 10으로 나눠떨어질면 (더한값 % 10 == 0) 유효한 숫자

T = int(input())
for i in range(1,T+1):
    num = [i for i in map(int,sys.stdin.readline().split())]
    odd = [num[0] * 2,num[2] * 2,num[4] * 2,num[6] * 2,num[8] * 2,num[10] * 2,num[12] * 2,num[14] *2]
    even = [num[1],num[3],num[5],num[7],num[9],num[11],num[13]]
    add = sum(even) + sum(odd)