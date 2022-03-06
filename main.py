from tokeniser import Tokeniser
from parser import Parser
from generator import Generator
import sys

output_file = "a.asm"
intput_file = sys.argv[1]

try:
    if "--help" in sys.argv:
        print("--help: shows you this")
        print("-o outputfile")
        exit()

    if "-o" in sys.argv:
        for index, arg in enumerate(sys.argv):
            if arg == "-o":
                output_file = sys.argv[index + 1]
                if index == 1:
                    intput_file = sys.argv[3]
except IndexError:
    print("Unknown console command")

read_file = open(intput_file, "r")
program = read_file.read()
read_file.close()

tokens = Tokeniser(program)
output = Parser(tokens)
print(output)
if output != "OK":
    exit()

asm = Generator(tokens)

write_file = open(output_file, "w")
write_file.write(asm)