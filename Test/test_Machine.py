from unittest import TestCase

from VM.Compiler.BytecodeBuilder import BytcodeBuilder
from VM.Machine import Machine


class TestMachine(TestCase):
    def test_run_simple_program_all_in_stack(self):
        builder = BytcodeBuilder()
        machine = Machine(
            bytecode = builder.generate_from_lines([
                    "PUSH 1",
                    "PUSH 2",
                    "IADD",
                    "HALT"
                ]))
        machine.step()
        assert machine.dump()["Stack"][0] == 1

        machine.step()
        assert machine.dump()["Stack"][0] == 2

        machine.step()
        assert machine.dump()["Stack"][0] == 3
    def test_run_STR(self):
        builder = BytcodeBuilder()
        machine = Machine(
            bytecode=builder.generate_from_lines([
                "PUSH 2",
                "PUSH 0x00ff",
                "STR",
                "HALT"
            ]))

        machine.step()
        machine.step()
        machine.step()

        assert machine.dump()["Memory"][0x00ff] == 2
    def test_run_LOD(self):
        builder = BytcodeBuilder()
        machine = Machine(
            bytecode=builder.generate_from_lines([
                "PUSH 2",
                "PUSH 0x00ff",
                "STR",
                "PUSH 0x00ff",
                "LOD",
                "HALT"
            ]))
        machine.step()
        assert machine.dump()["Stack"][0] == 2


