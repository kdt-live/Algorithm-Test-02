# 직사각형 길이 찾기
T=int(input())
for tc in range(T):
    length=list(map(int,input().split()))
    # 직사각형 성질에 착안 중복시 제거하여 1개만 남겨놓을 리스트 생성
    li=[]
    for value in length:
        if value not in li:
            li.append(value)
        else:
            li.remove(value)
    st=li[0]
    print(f'#{tc+1} {st}')