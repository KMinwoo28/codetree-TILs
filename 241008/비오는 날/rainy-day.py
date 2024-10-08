class weather:
    def __init__(self, date, week, cond):
        self.date = tuple(date.split('-'))
        self.week = week
        self.cond = cond
    
n = int(input())
lst = []
for i in range(n):
    date, week, cond = input().split()
    if cond == 'Rain':
        lst.append(weather(date, week, cond))

lst.sort(key = lambda x : (x.date[0], x.date[1], x.date[2]))
print('-'.join(lst[0].date), lst[0].week, lst[0].cond)