# 최빈수 구하기

# 비교용 list
compli=[]

# dictionary 사용하려 했으나 포기
# compdic={}

# cnt 담는 list. 빈도수 저장용
newli=[]

testli=[]

T=int(input())
for tc in range(1,T+1):
    times=int(input())
    score=list(map(int,input().split()))
    print('-------------------------------------------------------------')
    print('-------------------------------------------------------------')    
    # 자꾸 range 에러나서 뭐가 문젠지 찾기 위해 작성한 test list
    # score의 value로 만들었어야 했음. 리스트에 for를 몇 번이나 걸다보니 헷갈려 꼬인 이슈..
    # for indx in score:
    #     if indx not in testli:
    #         testli.append(indx)
    # print(testli)

    # 빈도수를 담기 위해 newli의 index를 점수에 맞춰 101개로 만들었음. 0~100.
    for e in range(101):
        newli.append(0)
    print(newli, len(newli))
    #newli 잘 만들었는지 확인용
    #print(newli)
    
    # 자꾸 인덱스 에러 나서 포기한 for문. 왠지 모르겠음.
    # IndexError: list index out of range
    # 왜지? newli의 인덱스는 compli[i]의 범위인 0~100인데.
    # compli 얘는 score list의 값을 중복 제거한 값이므로
    # len(score)=1000이고 len(compli)는 아 여기서 100이구나... 없는 점수가 있을 수 있네.
    # 오키.
    # 위 발상 틀림. 101개 맞고, for i in range(len(score))하면 0부터 999까지 1000이 나옴.
    # 범위 설정 실수.
    # for i in range(len(score)):
    #     if score[i] not in compli:
    #         compli.append(score[i])
    #     elif score[i] in compli:
    #         newli[compli[i]]+=1

    # score list의 value만 뽑아서 중복제거 list인 compli에 append함.
    # 또, compli는 중복 제거 list인데, value마다 동점자 몇명인지 체크하기 위해
    # cnt 저장용 list인 newli에 중복될 때마다 1점씩 추가.
    for element in score:
        if element not in compli:
            compli.append(element)
        elif element in compli:
            newli[element]+=1
            # compdic[score[i]]=0
            # compdic[score[i]]+=1
print(compli)
print('---------------------')
print(newli)

# 이제 newli의 index간 값 비교하고, 가장 높은 것만 출력하면 되는데.. index 어케쓰더라..
# maxv=max(newli.index())

# 걍 index없이 풀어봄.
cnt=0
st=newli[0]
for num in range(len(newli)):
    try:
        if st<newli[num+1]:
            st=newli[num+1]
            cnt=num
    except:
        pass
print(max(newli),cnt,compli[71])