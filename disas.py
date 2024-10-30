import sys

opcodes = {0: ["CSTI", 1],
1: ["ADD", 0],
2: ["SUB", 0],
3: ["MUL", 0],
4: ["DIV", 0],
5: ["MOD", 0],
6: ["EQ", 0],
7: ["LT", 0],
8: ["NOT", 0],
9: ["DUP", 0],
10: ["SWAP", 0],
11: ["LDI", 0],
12: ["STI", 0],
13: ["GETBP", 0],
14: ["GETSP", 0],
15: ["INCSP", 1],
16: ["GOTO", 1],
17: ["IFZERO", 1],
18: ["IFNZRO", 1],
19: ["CALL", 2],
20: ["TCALL", 3],
21: ["RET", 1],
22: ["PRINTI", 0],
23: ["PRINTC", 0],
24: ["LDARGS", 0],
25: ["STOP", 0]}

with open(sys.argv[1], "r") as f:
    program = list(map(int, f.read().split()))

pc = 0
while (pc < len(program)):
    c = opcodes[program[pc]]
    mnemonic, args = c[0], c[1]
    
    print(f"[PC: {str(pc).rjust(2, '0')}]: {mnemonic}", end=" ")

    for imm in range(args):
        print(program[pc + 1 + imm], end=" ")
    print()

    pc += args + 1
