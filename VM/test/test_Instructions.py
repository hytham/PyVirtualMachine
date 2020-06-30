from unittest import TestCase


from VM.Compiler.Instructions import Instructions, InstructionSet
from VM.Ports.PortControllers import tty1

from VM.VMContext import VMContext


class TestInstructions(TestCase):
    def test_get_by_opcode(self):
        ctx = VMContext()
        ins = Instructions(ctx)
        assert ins.getByOpcode(0xFF) == "HALT"

    def test_runHalt(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ins.halt()
        assert True

    def test_ipush(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.code.append(1)
        ctx.code.append(1)

        ins.push()

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_iadd(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(1)
        ctx.push(1)

        ins.iadd()

        assert ctx.SP == 1
        assert ctx.stack[0] == 2

    def test_isub(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.push(2)
        ctx.push(1)
        ins.isub()
        assert ctx.SP == 1
        assert ctx.stack[0] == -1

    def test_ieql(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.push(1)
        ctx.push(1)
        ins.ieql()
        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_ilt(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.push(2)
        ctx.push(1)

        ins.ilt()

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_igt(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.push(1)
        ctx.push(2)
        ins.igt()
        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_iadx(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.push(1)
        ctx.code.append(3)
        ctx.code.append(1)

        ins.iadx()

        assert ctx.SP == 1
        assert ctx.stack[0] == 2

    def test_isbx(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.push(2)

        ctx.code.append(5)
        ctx.code.append(1)

        ins.isbx()

        assert ctx.SP == 1
        assert ctx.stack[0] == -1

    def test_imul(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(2)
        ctx.push(2)

        ins.imul()

        assert ctx.SP == 1
        assert ctx.stack[0] == 4

    def test_imlx(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(2)

        ctx.code.append(7)
        ctx.code.append(2)

        ins.imlx()

        assert ctx.SP == 1
        assert ctx.stack[0] == 4

    def test_idiv(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(2)
        ctx.push(2)

        ins.idiv()

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_idvx(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(2)

        ctx.code.append(8)
        ctx.code.append(2)

        ins.idvx()

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_jmp(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)
        ctx.code.append(1)
        ctx.code.append(5)
        ctx.push(5)
        ctx.code.append(14)
        ctx.code.append(10)
        ctx.code.append(10)
        ctx.code.append(10)
        ctx.code.append(10)
        ctx.code.append(10)
        ctx.code.append(0xff)

        ins.jmp()

        assert ctx.IP == 5
        assert ctx.code[ctx.IP] == 10

    def test_jpe(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(15)
        ctx.push(1)

        ins.jpe()

        assert ctx.IP == 15

    def test_jpn(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(15)
        ctx.push(0)

        ins.jpn()

        assert ctx.IP == 15

    def test_store(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(10)
        ctx.push(100)

        ins.mrmstore()

        assert ctx.memory[100] == 10

    def test_load(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(10)
        ctx.push(100)
        ins.mrmstore()

        ctx.push(100)
        ins.memload()

        assert ctx.stack[0] == 10

    def test_global_store(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(10)
        ctx.push(100)

        ins.global_store()

        assert ctx.globals[100] == 10

    def test_port_load(self):
        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(0)

        ins.port_read()

        assert ctx.stack[0] == -1

    def test_port_store(self):

        ctx = VMContext()
        ins = InstructionSet(ctx)

        ctx.push(10)
        ctx.push(0)
        ins.port_write()

        assert True

    def test_call(self):
