from VM.Ports.PortControllers import tty1


class InstructionSet:

    def GetAllPorts(self):
        return [
            tty1
        ]

    def __init__(self, context):
        self.context = context

    def halt(self):
        """ HALT Operation meaning end of the code"""
        pass

    def nop(self):
        pass

    def push(self):
        """ push the next byte to the stack and increment the stack pointer by 1 """
        self.context.IP += 1
        a = self.context.code[self.context.IP]
        self.context.push(a)

    def iadd(self):
        """ Pop two int numbers from the stack and add them and push the result back to the stack """
        a = self.context.pop()
        b = self.context.pop()
        self.context.push(int(a) + int(b))

    def isub(self):
        """ Pop two numbers from the stack and push the subtracts of these two numbers to the stack """
        a = self.context.pop()
        b = self.context.pop()
        self.context.push(int(a) - int(b))

    def ieql(self):
        """ Pop Two numbers from the stack and push the result to the stack"""
        a = self.context.pop()
        b = self.context.pop()

        self.context.push(int(a == b))

    def ilt(self):
        """ Pop two number and check if the first is lesser than the later push the result to the stack"""
        a = self.context.pop()
        b = self.context.pop()

        self.context.push(int(a < b))

    def igt(self):
        """ Pop teo numbers from the stack and check the first is greater than the later and push to the stack"""
        a = self.context.pop()
        b = self.context.pop()

        self.context.push(int(a > b))

    def iadx(self):
        self.context.IP += 1
        a = self.context.code[self.context.IP]
        b = self.context.pop()
        self.context.push(int(a) + int(b))

    def isbx(self):
        self.context.IP += 1
        a = self.context.code[self.context.IP]
        b = self.context.pop()
        self.context.push(int(a) - int(b))

    def imul(self):
        a = self.context.pop()
        b = self.context.pop()

        self.context.push(int(a) * int(b))

    def imlx(self):
        self.context.IP += 1
        a = self.context.code[self.context.IP]
        b = self.context.pop()
        self.context.push(int(a) * int(b))

    def idiv(self):
        a = self.context.pop()
        b = self.context.pop()

        self.context.push(int(a) / int(b))

    def idvx(self):
        self.context.IP += 1
        a = self.context.code[self.context.IP]
        b = self.context.pop()
        self.context.push(int(a) / int(b))

    def jmp(self):
        address = self.context.pop()
        if address <= len(self.context.code):
            self.context.IP = address

    def jpe(self):
        flag = int(self.context.pop())
        if flag == 1:
            self.context.IP = int(self.context.pop())

    def jpn(self):
        flag = self.context.pop()
        if flag == 0:
            self.context.IP = self.context.pop()

    def mrmstore(self):
        address = self.context.pop()
        value = self.context.pop()
        self.context.memory[address] = value

    def memload(self):
        address = self.context.pop()
        value = self.context.memory[address]
        self.context.push(value)

    def global_load(self):
        address = self.context.pop()
        self.context.push(self.context.globals[address])

    def global_store(self):
        address = self.context.pop()
        value = self.context.pop()
        self.context.globals[address] = value

    def port_read(self):
        registred_ports = self.GetAllPorts()
        port_number = self.context.pop()
        target_port = registred_ports[port_number]()
        value = target_port.read()
        self.context.push(value)

    def port_write(self):
        registred_ports = self.GetAllPorts()
        port_number = self.context.pop()
        value = self.context.pop()
        registred_ports[port_number]().write(value)

    def port_exec(self):
        registred_ports = self.GetAllPorts()
        port_number = self.context.pop()
        registred_ports[port_number].execute()

    def fnccall(self):
        returnAddr = self.context.IP + 2;
        numArgs = self.context.code[self.context.IP]
        self.context.IP = self.context.IP + 1
        targetAddr = self.context.code[self.context.IP]
        self.context.IP = self.context.IP + 1
        self.context.Stack.Push(self.context.BP);
        self.context.Stack.Push(numArgs);
        self.context.Stack.Push(returnAddr);

        self.context.SP += 3;
        self.context.BP = self.context.SP;

        self.context.IP = targetAddr;

    def call_return(self):
        backupStack = []
        currentSP = self.context.SP

        for i in range(self.context.BP, currentSP):
            val = self.context.pop();
            backupStack.append(val);
            self.context.SP = self.context.SP - 1

        returnAddr = self.context.pop()
        numArgs = self.context.pop()
        self.context.BP = self.context.pop()

        while (numArgs > 0):
            self.context.pop()
            numArgs -= 1

        while (backupStack.Count > 0):
            self.context.push(backupStack.pop())

        backupStack = []

        self.context.IP = returnAddr;


class Instructions:
    def __init__(self, context):
        instSet = InstructionSet(context)
        self.Inst = [
            # Opcode, Mnumonic, action, number of expected arguments
            ("PUSH", 0x01, lambda x: instSet.push(), 1),  # PUSH 0x11
            ("IADD", 0x02, lambda x: instSet.iadd(), 0),  # IADD
            ("IADX", 0x03, lambda x: instSet.iadx(), 1),  # IADX 3
            ("ISUB", 0x04, lambda x: instSet.isub(), 0),  # ISUB
            ("ISBX", 0x05, lambda x: instSet.isbx(), 0),  # ISBX
            ("IMUL", 0x06, lambda x: instSet.imul()),  # IMUL
            ("IMLX", 0x07, lambda x: instSet.imlx(), 1),  # IMLX 0x11
            ("IDIV", 0x08, lambda x: instSet.idiv()),  # IDIV
            ("IDVX", 0x09, lambda x: instSet.idvx(), 1),  # IDVX
            ("NOP", 10, lambda x: instSet.nop(), 0),
            ("IEQL", 11, lambda x: instSet.ieql(), 0),
            ("ILT", 12, lambda x: instSet.ilt(), 0),
            ("IGT", 13, lambda x: instSet.igt(), 0),
            ("JMP", 14, lambda x: instSet.jmp(), 0),
            ("JPE", 15, lambda x: instSet.jpe(), 0),
            ("JPN", 16, lambda x: instSet.jpn(), 0),
            ("STR", 17, lambda x: instSet.mrmstore(), 0),
            ("LOD", 18, lambda x: instSet.memload(), 0),
            ("GLOD", 19, lambda x: instSet.global_load(), 0),
            ("GSTR", 20, lambda x: instSet.global_store(), 0),
            ("PTLD", 21, lambda x: instSet.port_read(), 0),
            ("PTST", 22, lambda x: instSet.port_write(), 0),
            ("PTEX", 23, lambda x: instSet.port_exec(), 0),
            ("CALL", 24, lambda x: instSet.fnccall(), 1),
            ("RET", 25, lambda x: instSet.call_return(),0),
            ("HALT", 0xFF, lambda x: instSet.halt(), 0)
        ]

    def getByOpcode(self, byte):
        for c in self.Inst:
            if c[1] == byte:
                return c[0]

        return -1

    def getActionByMnumonic(self, bytecode):
        """ get the action for a specific opcode"""
        for c in self.Inst:
            if c[1] == bytecode:
                return c[2]

        return None

    def getInstForOpcode(self, opcode):
        for c in self.Inst:
            if c[0] == opcode:
                return c[1], c[3]
