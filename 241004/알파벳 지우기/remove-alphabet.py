s1 = input()
s2 = input()

s1_lst = ''
s2_lst = ''
for i in range(len(s1)):
    if s1[i].isnumeric():
        s1_lst += s1[i]

for i in range(len(s2)):
    if s2[i].isnumeric():
        s2_lst += s2[i]

print(int(s1_lst) + int(s2_lst))