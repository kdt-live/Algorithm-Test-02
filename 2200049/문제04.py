T = int(input())
for i in range(T):
  str = input()
  nstr=''
  for s in reversed(str):
    if s=='p':
      nstr+='q'
    elif s=='q':
      nstr+='p'
    elif s=='b':
      nstr+='d'
    elif s=='d':
      nstr+='b'
  print(f"#{i+1}",nstr)