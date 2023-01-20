# 직사각형 길이 찾기
T = int(input())
for t in range(T):
	list_ = list(map(int, input().split()))
	dict_ = {}
	for i in list_:
		dict_[i] = list_.count(i)
	res = sorted(dict_.items(), key= lambda x: x[1])
	print(res)
	print(f'#{t+1}',res[0][0])



	