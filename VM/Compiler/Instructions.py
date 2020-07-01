from VM.Ports.PortControllers import tty1


class InstructionSet:

    def GetAllPorts(self):
        return [
            tty1
        ]




    def halt(self, context):
        """ HALT Operation meaning end of the code"""
        pass

    def nop(self, context):
        pass

    def push(self, context):
        """ push the next byte to the stack and increment the stack pointer by 1 """
        context.IP += 1
        a = context.code[context.IP]
        context.push(a)

    def iadd(self, context):
        """ Pop two int numbers from the stack and add them and push the result back to the stack """
        a = context.pop()
        b = context.pop()
        context.push(int(a) + int(b))

    def isub(self, context):
        """ Pop two numbers from the stack and push the subtracts of these two numbers to the stack """
        a = context.pop()
        b = context.pop()
        context.push(int(a) - int(b))

    def ieql(self, context):
        """ Pop Two numbers from the stack and push the result to the stack"""
        a = context.pop()
        b = context.pop()

        context.push(int(a == b))

    def ilt(self, context):
        """ Pop two number and check if the first is lesser than the later push the result to the stack"""
        a = context.pop()
        b = context.pop()

        context.push(int(a < b))

    def igt(self, context):
        """ Pop teo numbers from the stack and check the first is greater than the later and push to the stack"""
        a = context.pop()
        b = context.pop()

        context.push(int(a > b))

    def iadx(self, context):
        context.IP += 1
        a = context.code[context.IP]
        b = context.pop()
        context.push(int(a) + int(b))

    def isbx(self, context):
        context.IP += 1
        a = context.code[context.IP]
        b = context.pop()
        context.push(int(a) - int(b))

    def imul( self,context):
        a = context.pop()
        b = context.pop()

        context.push(int(a) * int(b))

    def imlx(self, context):
        context.IP += 1
        a = context.code[context.IP]
        b = context.pop()
        context.push(int(a) * int(b))

    def idiv(self, context):
        a = context.pop()
        b = context.pop()

        context.push(int(a) / int(b))

    def idvx(self, context):
        context.IP += 1
        a = context.code[context.IP]
        b = context.pop()
        context.push(int(a) / int(b))

    def jmp(self, context):
        address = context.pop()
        if address <= len(context.code):
            context.IP = address

    def jpe(self, context):
        flag = int(context.pop())
        if flag == 1:
            context.IP = int(context.pop())

    def jpn(self,context):
        flag = context.pop()
        if flag == 0:
            context.IP = context.pop()

    def mrmstore(self, context):
        address = context.pop()
        value = context.pop()
        context.memory[address] = value

    def memload(self, context):
        address = context.pop()
        value = context.memory[address]
        context.push(value)

    def global_load(self, context):
        address = context.pop()
        context.push(context.globals[address])

    def global_store(self, context):
        address = context.pop()
        value = context.pop()
        context.globals[address] = value

    def port_read(self, context):
        registred_ports = self.GetAllPorts()
        port_number = context.pop()
        target_port = registred_ports[port_number]()
        value = target_port.read()
        context.push(value)

    def port_write(self, context):
        registred_ports = self.GetAllPorts()
        port_number = context.pop()
        value = context.pop()
        registred_ports[port_number]().write(value)

    def port_exec(self, context):
        registred_ports = self.GetAllPorts()
        port_number = context.pop()
        registred_ports[port_number].execute()

    def fnccall(self, context):
        returnAddr = context.IP + 2;
        numArgs = context.code[context.IP]
        context.IP = context.IP + 1
        targetAddr = context.code[context.IP]
        context.IP = context.IP + 1
        context.Stack.Push(context.BP);
        context.Stack.Push(numArgs);
        context.Stack.Push(returnAddr);

        context.SP += 3;
        context.BP = context.SP;

        context.IP = targetAddr;

    def call_return(self, context):
        backupStack = []
        currentSP = context.SP

        for i in range(context.BP, currentSP):
            val = context.pop();
            backupStack.append(val);
            context.SP = context.SP - 1

        returnAddr = context.pop()
        numArgs = context.pop()
        context.BP = context.pop()

        while (numArgs > 0):
            context.pop()
            numArgs -= 1

        while (backupStack.Count > 0):
            context.push(backupStack.pop())

        backupStack = []

        context.IP = returnAddr;


class Instructions:
    def __init__(self):
        instSet = InstructionSet()
        self.Inst = [
            # Opcode, Mnumonic, action, number of expected arguments
            ("PUSH", 0x01, lambda x: instSet.push(x), 1),  # PUSH 0x11
            ("IADD", 0x02, lambda x: instSet.iadd(x), 0),  # IADD
            ("IADX", 0x03, lambda x: instSet.iadx(x), 1),  # IADX 3
            ("ISUB", 0x04, lambda x: instSet.isub(x), 0),  # ISUB
            ("ISBX", 0x05, lambda x: instSet.isbx(x), 0),  # ISBX
            ("IMUL", 0x06, lambda x: instSet.imul(x)),  # IMUL
            ("IMLX", 0x07, lambda x: instSet.imlx(x), 1),  # IMLX 0x11
            ("IDIV", 0x08, lambda x: instSet.idiv(x)),  # IDIV
            ("IDVX", 0x09, lambda x: instSet.idvx(x), 1),  # IDVX
            ("NOP", 10, lambda x: instSet.nop(x), 0),
            ("IEQL", 11, lambda x: instSet.ieql(x), 0),
            ("ILT", 12, lambda x: instSet.ilt(x), 0),
            ("IGT", 13, lambda x: instSet.igt(x), 0),
            ("JMP", 14, lambda x: instSet.jmp(x), 0),
            ("JPE", 15, lambda x: instSet.jpe(x), 0),
            ("JPN", 16, lambda x: instSet.jpn(x), 0),
            ("STR", 17, lambda x: instSet.mrmstore(x), 0),
            ("LOD", 18, lambda x: instSet.memload(x), 0),
            ("GLOD", 19, lambda x: instSet.global_load(x), 0),
            ("GSTR", 20, lambda x: instSet.global_store(x), 0),
            ("PTLD", 21, lambda x: instSet.port_read(x), 0),
            ("PTST", 22, lambda x: instSet.port_write(x), 0),
            ("PTEX", 23, lambda x: instSet.port_exec(x), 0),
            ("CALL", 24, lambda x: instSet.fnccall(x), 1),
            ("RET", 25, lambda x: instSet.call_return(x),0),
            ("HALT", 0xFF, lambda x: instSet.halt(x), 0)
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
