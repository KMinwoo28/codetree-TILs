a, b, c = map(int,input().split())
#if a<11 or (a == 11 and b<11):
#    print(-1)
#else:
s = (a*24*60 + b*60 + c) - (11*24*60 + 11*60 + 11) 
if s < 0:
    print(-1)
else:
    print(s)