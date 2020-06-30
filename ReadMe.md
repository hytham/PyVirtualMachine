### Py Virtual Machine
This is a POC Virtual machine writen completly in python, it is not intended for any real project just for me to learn a
how stack based vm works (VM in general)

#### VM Architecture
This VM is based on a:
* A stack that will push and pop integers. 
* A memory array of size 4M.
* A global storage a 255 byte to store global seetings
* A code storage that will save the running code
* PortController: is the way that VM will comunicate with outside , there 255 ports
* IP: Instruction pointer
* SP: a stack pointer 
* BP and abase pointer

Everything is pushed and poped to teh stack, this VM implments these instruction sets:

**PUSH[1]:**
`PUSH 1 ` push an integer to the stack

**IADD[2]:**
`IADD` pop two values from teh stack add them and push the result back to the stack

**IADX[3]:**
`IADX 1` this will add the value 1 to thae value that is in the stack and push the result to the stack


**ISUB[4]:**:
`ISUB` this pop two values from the stack and push the subtraction result to the stack

**ISBX[5]:**:
`ISBX 1` this will read the next byte in the code and pop from the stack, add them together and push the result back to the stack

**IMUL[6]:**:
`IMULT` pop tow values from the stack multiply them and push the result back

**IMLX[7]:**: 
`IMLX 1`pop a value from the stack and multiply it with next byte
in code 

**IDIV[8]:**
`IDIV` pop two values from the stack divid them and push the m back

**IDVX[9]:**
`IDVX 1` pop a value from the stack and devid it with next byte in the code

**NOP[10]:**
`NOP` No execution will happen to pass a single cycle
**IEQL[11]:**
`IEQL` pop two values from tenh stack and check if the are  equal push to the stack 1 if yes 0 if not

**ILT[12]:**
`ILT` pop two values from the stack check if the right side is lesser than the lefts side
push 1 if the left side is greater than 

**IGT[13]:**
`IGT` pop two values from the stack and test if the first is greater than the second, 1 will be pushed if true 0 else

**JMP[14]:**
'JMP' pop 1 values from the stack if the address is lesser than code size it will update the IP with new address

**JPE[15]:**
'JPE' pop 5 values from the stack 4(address) + value , if the value is 1 it will jump to the new address

**JPN[16]:**
`JPN` pop 5 values from the stack 4(address) + value, if the value is 0 jump to the new address

**STR[17]:**
`STR` pop 2  values from the stack address + value, write the value to the memory address specified

**LOD[18]:**
`LOD` pop a value from the stack will be the address , read the value from the memory location and push it to the stack

**GLOD[19]:**
`GLOAD` pop 2 values from the stack (2 address), read the values in the global storage and push it to the stack

**GSTR[20]:**
`GSTR` pop 3 values nfrom the stack (2 address) + value, save the value to the global storage

**PTLD[21]:**
`PTLD` pop 1 value from the stack that will represent the port number. then read the value
from the port and push it to the stack

**PTST[22]:**
`PTST` pop 2 values from the stack, write value to the ports with port number

**CALL[23]:**
`CALL` pop n value from the stack and update the IP to the new code segment, details TBD

**RET[24]:**
`RET` pop n values from the stack and update the IP to calling sunroutine address+ n, details TBD

**HALT[0xff]:**
'HALT' halt the execution and stop the VM 

### Bytecodebuilder.py
is a simple script that will take VM assembaly code and gendrate a bytecode



