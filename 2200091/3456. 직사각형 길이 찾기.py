test = int(input())

for i in range(test):
    # 세 변 길이를 리스트로 저장
    side = list(map(int, input().split()))
    tmp = {}

    # 각 길이가 몇 번 등장했는지 딕셔너리에 저장
    for j in side:
        if j in tmp:
            tmp[j] += 1
        else:
            tmp[j] = 1
    
        
    # 만약 직사각형이라면 한 번 등장한 길이가 출력
    # 정사각형이라면 세 번 등장한 길이가 출력
    for j in tmp:
        if tmp[j] != 2:
            print(f"#{i+1} {j}")
            break