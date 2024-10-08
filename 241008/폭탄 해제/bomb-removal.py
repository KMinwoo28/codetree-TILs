class bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time
    
    def nprint(self):
        print('code :',self.code)
        print('color :',self.color)
        print('second :',self.time)

c = input().split()
b = bomb(c[0],c[1], int(c[2]))
b.nprint()