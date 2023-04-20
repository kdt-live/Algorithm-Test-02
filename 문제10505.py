result2print = []
for x in range(int(input())) :
    N = int(input())
    list_num = list( map( int, input().strip().split(sep=" ") ) )
    list_num.sort()
    mean_value = int(sum(list_num)/N)
    result = 0
    for i in range(N-1, -1, -1) :
        if list_num[i] <= mean_value :
            result = i+1
            break
    result2print.append(f"#{x+1} {result}")
print("\n".join(result2print))