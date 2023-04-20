t = int(input())
for i in range(1, t+1) :
    n = input()
    n_list = list(n)
    for x in n_list :
        if x == "-":
            n_list.remove("-")
    n_list1 = list(map(int,n_list))
    for j in range(len(n_list1)) :
        if n_list1[0] != 3 and  n_list1[0] != 4 and n_list1[0] != 5 and n_list1[0] != 6 and n_list1[0] != 9 :
            print(f"#{i} {0}")
            break
        else :
            if len(n_list1) == 16 :
                print(f"#{i} {1}")
                break
            else :
                print(f"#{i} {0}")
                break
