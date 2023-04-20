 #  문자열의 거울상
T = int(input())

mirror_list = [input() for i in range(T)]

for i in range(T):
    mirror_list[i] = mirror_list[i][::-1] # 문자열을 뒤집고
    mirror_list[i] = mirror_list[i].replace('b','4') # b -> 4 -> d
    mirror_list[i] = mirror_list[i].replace('d', '2') # d -> 2 -> b
    mirror_list[i] = mirror_list[i].replace('p', '7') # q -> 6 -> p
    mirror_list[i] = mirror_list[i].replace('q', '6') # p -> 7 -> q
    mirror_list[i] = mirror_list[i].replace('4', 'd')
    mirror_list[i] = mirror_list[i].replace('2', 'b')
    mirror_list[i] = mirror_list[i].replace('7', 'q')
    mirror_list[i] = mirror_list[i].replace('6', 'p')

    print(f'#{i+1} {mirror_list[i]}')

# 이 방법 말고 더 좋은 방법이 있을텐데 문제푸는 당시에는 생각이 나지 않았다.
