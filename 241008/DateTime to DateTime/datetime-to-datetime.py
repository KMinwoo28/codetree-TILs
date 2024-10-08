a, b, c = map(int,input().split())
if b<11 or (b == 11 and c<11):
    print(-1)
else:
    print((a*24*60 + b*60 + c) - (11*24*60 + 11*60 + 11) )