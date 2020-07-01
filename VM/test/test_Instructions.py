from unittest import TestCase


from VM.Compiler.Instructions import Instructions, InstructionSet
from VM.Ports.PortControllers import tty1

from VM.VMContext import VMContext


class TestInstructions(TestCase):
    def test_get_by_opcode(self):

        ins = Instructions()
        assert ins.getByOpcode(0xFF) == "HALT"

    def test_runHalt(self):
        ctx = VMContext()
        ins = InstructionSet()
        ins.halt(ctx)
        assert True

    def test_ipush(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.code.append(1)
        ctx.code.append(1)

        ins.push(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_iadd(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(1)
        ctx.push(1)

        ins.iadd(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 2

    def test_isub(self):
        ctx = VMContext()
        ins = InstructionSet()
        ctx.push(2)
        ctx.push(1)
        ins.isub(ctx)
        assert ctx.SP == 1
        assert ctx.stack[0] == -1

    def test_ieql(self):
        ctx = VMContext()
        ins = InstructionSet()
        ctx.push(1)
        ctx.push(1)
        ins.ieql(ctx)
        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_ilt(self):
        ctx = VMContext()
        ins = InstructionSet()
        ctx.push(2)
        ctx.push(1)

        ins.ilt(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_igt(self):
        ctx = VMContext()
        ins = InstructionSet()
        ctx.push(1)
        ctx.push(2)
        ins.igt(ctx)
        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_iadx(self):
        ctx = VMContext()
        ins = InstructionSet()
        ctx.push(1)
        ctx.code.append(3)
        ctx.code.append(1)

        ins.iadx(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 2

    def test_isbx(self):
        ctx = VMContext()
        ins = InstructionSet()
        ctx.push(2)

        ctx.code.append(5)
        ctx.code.append(1)

        ins.isbx(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == -1

    def test_imul(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(2)
        ctx.push(2)

        ins.imul(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 4

    def test_imlx(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(2)

        ctx.code.append(7)
        ctx.code.append(2)

        ins.imlx(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 4

    def test_idiv(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(2)
        ctx.push(2)

        ins.idiv(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_idvx(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(2)

        ctx.code.append(8)
        ctx.code.append(2)

        ins.idvx(ctx)

        assert ctx.SP == 1
        assert ctx.stack[0] == 1

    def test_jmp(self):
        ctx = VMContext()
        ins = InstructionSet()
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

        ins.jmp(ctx)

        assert ctx.IP == 5
        assert ctx.code[ctx.IP] == 10

    def test_jpe(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(15)
        ctx.push(1)

        ins.jpe(ctx)

        assert ctx.IP == 15

    def test_jpn(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(15)
        ctx.push(0)

        ins.jpn(ctx)

        assert ctx.IP == 15

    def test_store(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(10)
        ctx.push(100)

        ins.mrmstore(ctx)

        assert ctx.memory[100] == 10

    def test_load(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(10)
        ctx.push(100)
        ins.mrmstore(ctx)

        ctx.push(100)
        ins.memload(ctx)

        assert ctx.stack[0] == 10

    def test_global_store(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(10)
        ctx.push(100)

        ins.global_store(ctx)

        assert ctx.globals[100] == 10

    def test_port_load(self):
        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(0)

        ins.port_read(ctx)

        assert ctx.stack[0] == -1

    def test_port_store(self):

        ctx = VMContext()
        ins = InstructionSet()

        ctx.push(10)
        ctx.push(0)
        ins.port_write(ctx)

        assert True

    def test_call_and_ret(self):
        pass
