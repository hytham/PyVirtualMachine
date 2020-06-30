""" THE CPU Context contain all of the flags registers and pointers """


class VMContext:
    def __init__(self, memory_size=4000000):
        self.IP = 0x0000  # Instruction pointer
        self.SP = 0x00  # Stack Pointer
        self.BP = 0x0000  # Base pointer

        self.stack = []
        self.memory = [None] * memory_size
        self.globals = [None] * 255
        self.code =[]


    def push(self,value):
        self.stack.append(value)
        self.SP+=1

    def pop(self):
        val = self.stack.pop()
        self.SP-=1
        return val



