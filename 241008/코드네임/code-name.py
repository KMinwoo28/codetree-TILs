class person:
    def __init__(self, codename = "", score = 0):
        self.codename = codename
        self.score = score
    
lst = []
for i in range(5):
    c, s = input().split()
    lst.append(person(c,int(s)))

lst.sort(key = lambda x : x.score)
print(lst[0].codename, lst[0].score)