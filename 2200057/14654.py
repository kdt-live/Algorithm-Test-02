T = int(input())

for t in range(1, T+1):
    car_no = input()
    car_no = ''.join(list(car_no.split('-')))
    if car_no[0] in '34569' and len(car_no) == 16:
        print(f'#{t} 1')
        
    else:
        print(f'#{t} 0')
