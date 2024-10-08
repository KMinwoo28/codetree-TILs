d = [0,31,29,31,30,31,30,31,31,30,31,30,31]
yo = ['Mon','Tue','Wed',"Thu",'Fri','Sat','Sun']
m1, d1, m2, d2 = map(int,input().split())
l1 = sum([i for i in d[1:m1]]) + d1
l2 = sum([i for i in d[1:m2]]) + d2
dif = l2 - l1

t = input()
target = yo.index(t)

r = dif // 7
rem = dif % 7
if target - rem > 0:
    print(r)
else:
    print(r+1)