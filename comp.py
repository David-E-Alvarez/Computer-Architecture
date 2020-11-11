import sys

# Instructions are stored in RAM (memory)
# Behaves like an array of numbers

if len(sys.argv) != 2:
    print("usage: comp.py filename")
    sys.exit(1)

memory = [0] * 256

try:
    address = 0

    with open(sys.argv[1]) as f:
        for line in f:
            line = line.split()

            if line == [] or line[0] == '#':
                continue

            value = int(line[0])

            #print(repr(value))
            memory[address] = value

            address += 1

except FileNotFoundError:
    print(f"cannot open file {sys.argv[1]}")
    sys.exit(2)

register = [0] * 8   # Like variables, names R0, R1, R2 ... R7

pc = 0  # Index into memory of the currently-executing instruction


while True:

    instruction = memory[pc]

    if instruction == 1:  # PRINT_BEEJ
        print("Beej!")
        pc += 1

    elif instruction == 2:  # HALT
        pc += 1
        break

    elif instruction == 3:  # SAVE_REG
        reg_num = memory[pc + 1]
        value = memory[pc + 2]
        register[reg_num] = value

        #print(register)
        pc += 3

    elif instruction == 4:  # PRINT_REG
        reg_num = memory[pc + 1]
        print(register[reg_num])

        pc += 2

    elif instruction == 5:  # ADD
        reg_num_a = memory[pc + 1]  # if pc == 3, memory[3+1], memory[4]
        reg_num_b = memory[pc + 2]

        register[reg_num_a] += register[reg_num_b]

        pc += 3

    else:
        print(f"Unknown instruction {instruction} at address {pc}")
        sys.exit(1)

