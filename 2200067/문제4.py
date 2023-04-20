'''
문자열의 거울상
'''
t = int(input())
for i in range(1,t+1):
    s = input()
    reversed_s = s[::-1]
    if s:
        print(f'#{i} {reversed_s}')