# 문자열의 거울상
T=int(input())
for tc in range(T):
    word=input()
    # 리스트로 해야 할 지 문자열로 해야할지 몰라 일단 만들어둔 리스트
    wdli=[]
    for elements in word:
        wdli.append(elements)
    start=0
    end=len(word)-1
    # print(word, start, end)
    word_reverse=wdli[::-1]
    # replace 메소드 ㅠㅠㅠ어케 쓰더라 ㅠㅠㅠㅠㅠ
    # 메소드로 풀기도 연습해야겠다...하나도모르겠네..
    for i in range(len(word_reverse)):
        if word_reverse[i]=='d':
            word_reverse[i]='b'
        elif word_reverse[i]=='b':
            word_reverse[i]='d'
        elif word_reverse[i]=='p':
            word_reverse[i]='q'
        else:
            word_reverse[i]='p'
    # 세상에... print %d 사용법과, list->str 변환 방법 좀 공부해야겠다.
    # word_reverse=str(word_reverse)
    # print(type(word_reverse))
    # print(f'#{tc+1} {word_reverse}')
    print('#',end="")
    print(tc+1,end=" ")
    print(*word_reverse,sep="")