lastday = [31,0,31,30,31,30,31,31,30,31,30,31]
season = ['Winter','Spring','Summer','Fall']

def avail(y,m,d):
    yoon = False
    if y % 4 == 0:
        yoon = True
    elif y % 4 == 0 and y % 100 == 0:
        yoon = False
    elif y % 4 == 0 and y % 100 == 0 and y % 400 == 0:
        yoon = True
    if m != 2:
        if lastday[m - 1] < d:
            return -1
        else:
            return season[(m%12)//3]
    else:
        if yoon:
            if d > 29:
                return -1
        else:
            if d > 28:
                return -1
        return 'Winter'

Y, M, D = map(int,input().split())
print(avail(Y,M,D))