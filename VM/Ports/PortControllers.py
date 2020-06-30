
class tty1:
    def __init__(self):
        self.buffer = []
    def read(self):
        if len(self.buffer) > 0 :
            return  self.buffer.pop()
        return -1

    def write(self,value):
        self.buffer.append(value)

    def execute(self):
        print(str(self.buffer))