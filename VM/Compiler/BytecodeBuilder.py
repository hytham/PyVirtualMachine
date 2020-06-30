
from binascii import unhexlify
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

    def parse(self,lines):
            for line in lines:
                line_parts = line.split(' ')
                code = self.getOpcode(line_parts)
                for b in iter(code):
                    self.bytecode.append(b)

            return self.bytecode


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
                return [code, parts[1]]

        return [code]

    def long_to_bytes(self,val, endianness='big'):
        val = int(val,16)
        width = val.bit_length()

        # unhexlify wants an even multiple of eight (8) bits, but we don't
        # want more digits than we need (hence the ternary-ish 'or')
        width += 8 - ((width % 8) or 8)

        # format width specifier: four (4) bits per hex digit
        fmt = '%%0%dx' % (width // 4)

        # prepend zero (0) to the width, to zero-pad the output
        s = unhexlify(fmt % val)

        if endianness == 'little':
            # see http://stackoverflow.com/a/931095/309233
            s = s[::-1]

        return s
















