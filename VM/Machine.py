from VM.Compiler.Instructions import Instructions
from VM.Ports.PortControllers import tty1, tty2
from VM.VMContext import VMContext


class Machine:
    def __init__(self,bytecode = None,memory_size=1000000,debug = False):
        self.vm_context = VMContext(memory_size)
        self.vm_context.debug = debug

        self.vm_context.IP = 0
        self.vm_context.SP = 0
        self.vm_context.BP = 0

        self.vm_context.code = bytecode
        self.Instruction_table = Instructions()


    def run(self):
        if (self.vm_context.debug == True):
            print(self.dump())

        opcode = self.vm_context.code[self.vm_context.IP]
        while self.vm_context.IP < len(self.vm_context.code) | opcode != 0xff:
            opcode = self.step()

        if (self.vm_context.debug == True):
            print(self.dump())

        return 0

    def step(self):
        opcode = self.vm_context.code[self.vm_context.IP]
        if opcode !=0xff:
            action = self.Instruction_table.getActionByMnumonic(opcode)
            action(self.vm_context)

        self.vm_context.IP += 1

        if (self.vm_context.debug == True):
            print(self.dump())

        return opcode

    def dump(self):
        """ Dump the stack trace as it is"""
        return {
            "IP": self.vm_context.IP,
            "SP" : self.vm_context.SP,
            "OpCode": self.vm_context.code[self.vm_context.IP],
            "Stack": self.vm_context.stack,
            "Memory": self.vm_context.memory
        }



    def register_ports(self):
        controllers = [
            tty1,
            tty2
        ]







