#최빈수 구하기
import sys

T = int(sys.stdin.readline())
for t in range(T):
    num = sys.stdin.readline()
    list_ = list(map(int, str(sys.stdin.readline()).split()))
    dict_ = {}
    for i in list_:
        if i in dict_:
            dict_[i] += 1
        else:
            dict_[i] = 1
        max_key = max(dict_, key=dict_.get)
        

    print(f'#{t + 1}' , f'{str(max_key)}')

 
    