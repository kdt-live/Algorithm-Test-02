

# 테스트 케이스 수 : 2
# T = int(input())
# string = {
#     'b': 'p',
#     'd': 'q',
#     'p': ['b', 'q'],
#     'q': 'd'
# }
# S_list = [[], []]
# for t in range(1, T+1):
#     S = input()
#     for i in S:
#         S_list[0].append(i)
# print(S_list)

# bdppq -> pqqbd 로 바뀌는 경우
# 입력 케이스에서 규칙을 못찾겠음...
new = []
N = input()
for i in N:
    if i == 'b':
        new.append('p')
    elif i == 'd':
        new.append('q')
    elif i == 'p':
        new.append('b')
    else:
        new.append('d')

print(*new, sep="")
