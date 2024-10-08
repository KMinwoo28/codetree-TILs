class struct:
    def __init__(self, code, place, time):
        self.code=  code
        self.place = place
        self.time = time

    def nprint(self):
        print('secret code :', self.code)
        print('meeting point :', self.place)
        print('time :', self.time)

code = list(input().split())
s = struct(code[0],code[1], code[2])
s.nprint()