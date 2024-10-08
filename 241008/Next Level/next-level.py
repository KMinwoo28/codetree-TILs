class info:
    def __init__(self, Id = 'codetree', level = 10):
        self.Id = Id
        self.level = level

    def nprint(self):
        print(f'user {self.Id} lv {self.level}')

per1 = info()
n = input().split()
per2 = info(n[0], int(n[1]))
per1.nprint()
per2.nprint()