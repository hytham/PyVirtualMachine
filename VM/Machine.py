from VM.Compiler.Instructions import Instructions
from VM.Ports.PortControllers import tty1
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
        """ Run the virtual machine"""
        opcode = self.vm_context.code[self.vm_context.IP]

        if (self.vm_context.debug == True):
            print(self.dump())

        while self.vm_context.IP < len(self.vm_context.code) | opcode != 0xff:
            self.step(opcode)
            self.vm_context.IP += 1
            opcode = self.vm_context.code[self.vm_context.IP]

            if (self.vm_context.debug == True):
                print(self.dump())

        return 0


    def dump(self):
        """ Dump the stack trace as it is"""
        return {
            "IP": self.vm_context.IP,
            "SP" : self.vm_context.SP,
            "OpCode": self.vm_context.code[self.vm_context.IP],
            "Top Stack Value": self.vm_context.stack,
        }

    def step(self,opcode):
        action = self.Instruction_table.getActionByMnumonic(opcode)
        action(self.vm_context)

    def register_ports(self):
        controllers = [
            tty1
        ]







