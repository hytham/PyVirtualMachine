from unittest import TestCase

from VM.Compiler.BytecodeBuilder import BytcodeBuilder


class TestBytcodeBuilder(TestCase):
    def test_generate_from_lines(self):
        code = [
            "PUSH 1"
        ]

        builder = BytcodeBuilder()

        bytecode = builder.generate_from_lines(code)

        assert len(bytecode) == 2
        assert bytecode[0] == 1 & bytecode[1]==1

    def test_generate_from_lines_push_hex(self):
        code = [
            "PUSH 0x01"
        ]

        builder = BytcodeBuilder()

        bytecode = builder.generate_from_lines(code)

        assert len(bytecode) == 2
        assert bytecode[0] == 1 & bytecode[1] == 1

    def test_generate_from_lines_push_bin(self):
        code = [
            "PUSH 0b01"
        ]

        builder = BytcodeBuilder()

        bytecode = builder.generate_from_lines(code)

        assert len(bytecode) == 2
        assert bytecode[0] == 1 & bytecode[1] == 1

    def test_generate_from_lines_add_mixed(self):
        code = [
            "PUSH 0x01",
            "PUSH 0b01",
            "IADD"
        ]

        builder = BytcodeBuilder()
        bytecode = builder.generate_from_lines(code)

        assert len(bytecode) == 5
        assert bytecode[0] == 1 & bytecode[1] == 1
        assert bytecode[2] == 1 & bytecode[3] == 1
        assert bytecode[4] == 2

    def test_generate_from_lines_store_to_memory_mixed(self):
        code = [
            "PUSH 0xFFFFFF",
            "PUSH 0b100101",
            "STR"
        ]
        builder = BytcodeBuilder()
        bytecode = builder.generate_from_lines(code)

        assert len(bytecode) == 5
        assert bytecode[0] == 1
        assert bytecode[1] == 16777215
        assert bytecode[2] == 1
        assert bytecode[3] == 37
        assert bytecode[4] == 17

