import sys# to read a program 

if len(sys.argv) != 2:
    print("usage: comp2.py filename")
    sys.exit(1)

#1.) i need memory to store instructions
memory = [0] * 16

try:
    address = 0 #used to keep track of instructions to be executed
    with open(sys.argv[1]) as f:#opens up file
        for line in f:
            line = line.split()#make lines in file an array to parse out '#' signs
            if line == [] or line[0] == '#':
                continue
            print("line: ", line)
            value = int(line[0])
            print("value: ", value)
            memory[address] = value
            address += 1

except FileNotFoundError:
    print(f"cannot open file {sys.argv[1]}")
    sys.exit(2)


#2.) register holds values to be calculated on.
register = [0] * 8
#3.) index current instruction executing 
pc = 0
#4.) loop over program to read all instructions
while True:
    instruction = memory[pc]
    print("instruction: ", instruction)
    if instruction == 1:
        print("hello world...yay?")
        pc += 1
        break
    else:
        break