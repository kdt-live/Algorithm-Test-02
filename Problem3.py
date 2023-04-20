t = int(input())
for i in range(1, t+1) :
    case = input()
    case_list = list(case)
    case_list.reverse()
    case_change = []
    for j in case_list :
        if j  == "b" :
            case_change.append("d")
        elif j == "d" :
            case_change.append("b")
        elif j == "p" :
            case_change.append("q")
        else :
            case_change.append("p")
    result = "".join(case_change)
    print(f"#{i} {result}")