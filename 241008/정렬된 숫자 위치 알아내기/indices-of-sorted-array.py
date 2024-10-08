n = int(input())
lst = list(map(int,input().split()))
d = dict()
for i in range(n):
    d[i] = [lst[i], i]
#print(d)

new_l = sorted(d.values(), key = lambda x: x[0])
#print(new_l)
new_d = dict()
for i in range(n):
    new_d[i]= new_l[i] + [i]

#print(new_d)
new_d_2 = sorted(new_d.values(), key = lambda x: x[1])
#print(new_d_2)
for i in range(n):
    print(new_d_2[i][2] + 1, end = " ")