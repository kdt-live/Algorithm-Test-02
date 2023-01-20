import sys
sys.stdin = open("input.txt", "r")

test = int(sys.stdin.readline().strip())

for i in range(test):
    n = int(sys.stdin.readline().strip())
    # 학생들 점수를 리스트로 저장
    stu_list = list(map(int, sys.stdin.readline().split()))
    # 빈도수를 확인하기 위한 딕셔너리 생성
    stu_dict = {}

    # 점수가 딕셔너리에 없다면 새로운 key로 추가하고 value로 1을 저장
    # 이미 딕셔너리에 있다면 value 값에 1을 더하면서 빈도수를 측정
    for j in stu_list:
        if j in stu_dict:
            stu_dict[j] += 1
        else:
            stu_dict[j] = 1

    # 빈도수를 기준으로 딕셔너리 정렬
    stu_dict = sorted(stu_dict.items(), key=lambda x: x[1], reverse=True)
    
    print(f"#{n} {stu_dict[0][0]}")