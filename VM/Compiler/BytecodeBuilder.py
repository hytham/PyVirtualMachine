import re
from VM.Compiler.Instructions import Instructions


class BytcodeBuilder:
    def __init__(self):
        self.bytecode = []
        self.inst = Instructions()
    def generate(self,source_filename):
        with open(source_filename, 'r') as f:
            for line in f:
                line_parts = line.split(' ')
                code = self.getOpcode(line_parts)
                for b in iter(code):
                    self.bytecode.append(b)

        return self.bytecode

    def generate_from_lines(self,lines):
        bytecode = []
        for line in lines:
            line_parts = line.split(' ')
            code = self.getOpcode(line_parts)
            for b in iter(code):
                bytecode.append(b)

        return bytecode



    def save(self,filename):
        f = open(filename, 'w+b')
        byte_arr = self.bytecode
        binary_format = bytearray(byte_arr)
        f.write(binary_format)
        f.close()

    def getOpcode(self,parts):
        opcode =str.upper(parts[0])
        code , nargs = self.inst.getInstForOpcode(opcode)
        if nargs > 0:
            if parts[1].find('x') > 0:
                return [code, int(parts[1],base=16)]
            elif parts[1].find('b') > 0:
                return [code, int(parts[1],base=2)]
            else:
                return [code, int(parts[1])]

        return [code]




































