# 신용카드 만들기2
accept_number=['3','4','5','6','9']
T= int(input())
for tc in range(T):
    # input 카드 번호
    numbers=list(input())
    new=[]

        # # 실패한 시도들. replace 메소드 사용법을 숙지 못해서... 사용하려다 실패.
        # nli=[]
        # for e in range(len(numbers)):
        #     if numbers[e]=='-':
        #        for i in numbers:
        #         if i!='-':
        #           nli.append(i)
        # print(nli)
        # print(numbers)
        # print(nli) 
        # print(numbers) 

    # replace 메소드 사용법 몰라서 -를 제거한 list 생성. new list.
    for rmv in numbers:
        new.append(rmv)
        if rmv=='-':
            new.pop()
    # print(new)

 
    # 이중 for문 들어가기 전에 ans를 저장을 해놓아야 초기화 안 됨.
    ans=f'#{tc+1} 0'
    for acp in accept_number:
        # 길이조건
        if len(new)!=16:
            ans=f'#{tc+1} 0'
        # 성공조건
        elif new[0]==acp:
            ans=f'#{tc+1} 1'
    print(ans)
      



        # # # 실패한 시도들...


        # if numbers[0]!='3':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='4':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='5':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='6':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='9':
        #     print(f'#{tc+1} 0')
        # #길이조건
        # elif len(numbers)!=16:
        #     print(f'#{tc+1} 0')
        # #성공
        # else:
        #     print(f'#{tc+1} 1')



        # #리스트 첫자리가 3 4 5 6 9가 아닐 때 실패
        # if numbers[0]!='3':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='4':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='5':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='6':
        #     print(f'#{tc+1} 0')
        # elif numbers[0]!='9':
        #     print(f'#{tc+1} 0')
        # #길이조건
        # elif len(numbers)!=16:
        #     print(f'#{tc+1} 0')
        # #성공
        # else:
        #     print(f'#{tc+1} 1')