# 신용카드 만들기 1

T=int(input())
for tc in range(T):
    nums=list(map(int,input().split()))
    # print(nums)
    # 홀수자릿수 리스트
    odd=[]
    # 짝수자릿수 리스트
    even=[]
    # 홀수합 odd number
    on=0
    # 짝수합 even number
    en=0
    # on+en의 합 total
    total=0
    # k=total을 10으로 나눈 나머지
    k=0
    # 10-k는 구하고자 하는 N
    N=0
    for indx in range(8):
        on+=nums[indx*2]*2
        # print(indx*2)
        # print(f'{indx+1}번째 on은 {on}')
    for inde in range(1,8):
        en+=nums[inde*2-1]
        # print(f'{inde}번째 en은 {en}')
    total=on+en
    k=total%10
    N=10-k
    if N==10:
        N=0
    # print(f'on={on}, en={en}, total={total}, k={k}, N={N}')
    # print('----------------------------')
    print(f'#{tc+1} {N}')



# 자꾸 on 더하는 for문에서 에러 떠서 시도해봄.
# 에러 IndexError: list index out of range
# li=[]
# for i in range(15):
#     li.append(i)
# print(li)
# for indx in range(8):
#     print((indx*2+1))
# for e in range(8):
#     print(li[e*2]+1)