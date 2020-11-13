import sys# to read a program 

if len(sys.argv) != 2:
    print("usage: comp2.py filename")
    sys.exit(1)

try:

    with open(sys.argv[1]) as f:#opens up file
        for line in f:
            print(line)#print file contents

except FileNotFoundError:
    print(f"cannot open file {sys.argv[1]}")
    sys.exit(2)

#1.) i need memory to store instructions
memory = [0] * 16
#2.) register holds values to be calculated on
register = [0] * 8