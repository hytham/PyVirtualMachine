from VM.Compiler.BytecodeBuilder import BytcodeBuilder
from VM.Machine import Machine

source_code = [
    "PUSH 1",
    "PUSH 1",
    "IADD",
    "IADX 2",
    "HALT"
]

def main():

    bc_builder = BytcodeBuilder()

    code = bc_builder.parse(source_code)
    machine = Machine(bytecode=code,debug=True)
    machine.run()


if __name__ == "__main__":
    main()