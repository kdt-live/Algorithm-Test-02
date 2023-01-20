# 최빈수 구하기

T = int(input())

for t in range(1,T+1):
    a = int(input()) 
    score = list(map(int,input().split())) 
    
    num_dic = {} # 빈 딕셔너리 생성 

    for i in score:
        if i in num_dic:
            num_dic[i] += 1  # 값 있으면 +1 
        else:
            num_dic[i] = 1 # 값 없으면 그냥 1 

# print(dic)
        # 이후에 딕셔너리에서 Key 값이 가장 높은 value를 꺼내오고 싶었는데 
        # 어떻게 해야할지 모르겠어요 ㅜ

    # print(f'#{a} {(max(num_dic, }')