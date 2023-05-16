# define registers
registers = [0] * 8

# parse and execute each instruction
program = """
MV REG1, #2000
MV REG2, #4000
ADD REG1, REG2
ADD REG1, 600
SHOW REG1
"""

for line in program.split("\n"):
    # parse instruction
    parts = line.split(" ")
    if parts[0] == "MV":
        reg = int(parts[1][3])
        value = int(parts[2][1:])
        registers[reg] = value
    elif parts[0] == "ADD":
        reg1 = int(parts[1][3])
        if parts[2][0] == "R":
            reg2 = int(parts[2][3])
            registers[reg1] += registers[reg2]
        else:
            value = int(parts[2])
            registers[reg1] += value
    elif parts[0] == "SHOW":
        reg = int(parts[1][3])
        print(registers[reg])
