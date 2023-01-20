a=int(input())
dic={
    'b':'d',
    'd':'b',
    'q':'p',
    'p':'q'
}
for i in range(a):
    string=input()
    new_string=''
    for j in string:
        # arr.append(dic[j])
        new_string+=dic[j]
    # print('#'+str(i+1), arr[::-1])
    print('#'+str(i+1),new_string[::-1])
    