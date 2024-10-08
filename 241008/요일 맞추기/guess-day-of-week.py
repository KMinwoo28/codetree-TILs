d = [0,31,28,31,30,31,30,31,31,30,31,30,31]
yo = ['Mon','Tue','Wed',"Tur",'Fri','Sat','Sun']

m1, d1, m2, d2 = map(int,input().split())
l1 = sum([i for i in d[1:m1]]) + d1

l2 = sum([i for i in d[1:m2]]) + d2


dif = (l2 - l1)%7
print(yo[dif])