### Py Virtual Machine
This is a POC Virtual machine writen completly in python, it is not intended for any real project just for me to learn a
how stack based vm works (VM in general)

#### VM Architecture
This VM is based on a:
* A stack that will push and pop integers. 
* A memory array of size 4M.
* A global storage a 255 byte to store global settings.
* A code storage that will save the running code.
* Port Controller: is the way that VM will communicate with outside.
* IP,SP,BP: Machine pointers.

Everything is pushed and pooped to the stack, this VM implements these instruction sets:

**PUSH[0x01]:**
`PUSH 1 ` push an integer to the stack

**IADD[0x02]:**
`IADD` pop two values from the stack add them and push the result back to the stack

**IADX[0x03]:**
`IADX 1` this will add the value 1 to the value that is in the stack and push the result to the stack

**ISUB[0x04]:**:
`ISUB` this pop two values from the stack and push the subtraction result to the stack

**ISBX[0x05]:**:
`ISBX 1` this will read the next byte in the code and pop from the stack, add them together and push the result back to the stack

**IMUL[0x06]:**:
`IMULT` pop tow values from the stack multiply them and push the result back

**IMLX[0x07]:**: 
`IMLX 1`pop a value from the stack and multiply it with next byte
in code 

**IDIV[0x08]:**
`IDIV` pop two values from the stack divid them and push the m back

**IDVX[0x09]:**
`IDVX 1` pop a value from the stack and devid it with next byte in the code

**NOP[0x0A]:**
`NOP` No execution will happen to pass a single cycle
**IEQL[0x0B]:**
`IEQL` pop two values from tenh stack and check if the are  equal push to the stack 1 if yes 0 if not

**ILT[0x0C]:**
`ILT` pop two values from the stack check if the right side is lesser than the lefts side
push 1 if the left side is greater than 

**IGT[0x0D]:**
`IGT` pop two values from the stack and test if the first is greater than the second, 1 will be pushed if true 0 else

**JMP[0x0E]:**
'JMP' pop 1 values from the stack if the address is lesser than code size it will update the IP with new address

**JPE[0x0F]:**
'JPE' pop 5 values from the stack 4(address) + value , if the value is 1 it will jump to the new address

**JPN[0x10]:**
`JPN` pop 5 values from the stack 4(address) + value, if the value is 0 jump to the new address

**STR[0x11]:**
`STR` pop 2  values from the stack address + value, write the value to the memory address specified

**LOD[0x12]:**
`LOD` pop a value from the stack will be the address , read the value from the memory location and push it to the stack

**GLOD[0x13]:**
`GLOAD` pop 2 values from the stack (2 address), read the values in the global storage and push it to the stack

**GSTR[0x14]:**
`GSTR` pop 3 values nfrom the stack (2 address) + value, save the value to the global storage

**PTLD[0x15]:**
`PTLD` pop 1 value from the stack that will represent the port number. then read the value
from the port and push it to the stack

**PTST[0x16]:**
`PTST` pop 2 values from the stack, write value to the ports with port number

**CALL[0x17]:**
`CALL` pop n value from the stack and update the IP to the new code segment, details TBD

**RET[0x18]:**
`RET` pop n values from the stack and update the IP to calling sunroutine address+ n, details TBD

**HALT[0xFF]:**
'HALT' halt the execution and stop the VM 

#### Byte Code Builder
Is a simple script that will take VM assembly code and generate a bytecode, for now the 
file will just contain assembly code

#### The Machine Stack
The stack is an int-array that will store values between computations, also there is a stack pointer 
that will track the current index of the stack.
PUSH[0x01] is used to push values to the stack it will only accept a single operand that is the values 
that can bewritten in be passed as a Hex or  bin or a regular number
`PUSH 0x01` will oush the Hex value 1 to the stack, this will increment the SP by 1

#### The Machine Memory
Is 1M int-array that can be used to store int-values, to save values to the memory we must push 
first the value that will be stored then the memory location  and call STR[0x11] 
`PUSH 0x01 => PUSH 0x00ff =>  STR` we will push first the memory address 0x11ff to the stack first
then we will push 0x01 then will call STR that will save the value 0x01 to memory location 0x11ff

To read from memory we must push the memory address first then call LOD[0x12]
`PUSH 0x11ff  =>  LOD`, as first we are pushing the memory address to the stack, then calling
LOD that will pop read the value from 0x11ff and push it to the stack

#### The Machine Global Storage
This is a 255 size int-array that will hold seetings or any other temporary values it works the same 
as the Machine Memory but we will use GSTR[0x16] to save value to it and GLOD[0x15] to read the value from it.

#### The Machine Code Storage
This a dynamic array that will store the main program opcode, the main bytecode is the machine start
on this can call other bytecodes stored in memory.

#### Ports
Ports are a two way communication to communicate with the outside, there are 255 port. each port must implment 
three methods
* read_port: that will read a single value from the port
* write_port that will write a single value from the port
* execute_port: that will execute an action in the port
* register_port: that will be called first when the machine starts to register the port it self and init any actions by the port

To send a single value to the port we need to push the value then port number to the stack
then push the value and call PTST[0x16], to read a single value from the port we must push the port number
then call PTLD[0x15]

**read_port and write_port** is used as two way communication that will write data to the port
internal buffer

**execute_port** is a one way communication that will send commands ro the port. every port
must read or write to the buffer and execute the command that is received

**register_port** where we must register the port with the machine and start running a separate thread
to handle its internal life cycle that include interpreting the commands that is being send by the machine  


### Machine Pointer:
There are 3 main pointers that will tack the current index of each value
* IP: Instruction pointer that will hold the current location of the head in the code storage
* SP: Stack pointer that will hold the current location of the head in the stack
* BP: Base pointer is ude when we are calling a sub routine


#### Machine Ports:
##### tty1 [0]:
This is a simple terminal that will display string on the host console


##### tty2 [1]:
This is a simple terminal that will display string on the host console



##### graph[0x0A]
This port will send message a virtual screen to plot on it


#### net[0x1A]
This port will send and receive data using sockets

#### p2p[0x1B] 
This port will send and receive data over p2p network



 
### The Machine High level language
This machine is equiped with its own simple Language 
That have the following keywords
 * var: a variable deceleration, the value will be saved in the machine memory 
 * const: a variable deceleration, the value will be saved in the machine memory 
 * if-else:
 * print:
 
  The language is based on this grammar
 ```buildoutcfg
letter : "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p"
       | "q" | "r" | "s" | "t" | "u" | "v" | "w"
       | "x" | "y" | "z" 
digit : "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" 
symbol : "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
       | "'" | '"' | "=" | "|" | "." | "," | ";" 
character : letter | digit | symbol | "_" 
number = digit+;
string = '"' , { character - '"' }, '"' ;
boolean = "True" | "False"
WS = "/s+"
logic = "&" | "|" | "!"
math = "+" | "-" | "*" | "/" | "\\" | "%"
escape = "\'" | "\"" | "\\" | "\n" | "\r" | "\t" | "\b" | "\f" | "\v" | "\0" | "0xFF"
number_litrals = "b" digits | "0x" digits  

program = Staments
Statment = LANGStatment | IFStatment | FORStatment | LogicStatment
           FUNCStatment 
            
LOGICStatment = expression logic expression
FUNCStatment = "func" FUNCNAME "(" PARAMETERS ")" ":" DataType
FUNCNAME = string
PARAMETERS = Identifier WS datatype "," | Identifier WS  datatype
LANGStatment = TypeId Identifier ":" DataType = expression 

FORStatment = "for" Identifier "from" digit "to" digit "step" digit "{" Statments "}"
IFStatment =  "if" expresson { statments } 


TypeId = var | const
Identifier = letter , { letter | digit | "_" }
Datatype = "int" | "float" | "bool" | "string"
expression = number, "+", number, ";"
expression = "if"





```

