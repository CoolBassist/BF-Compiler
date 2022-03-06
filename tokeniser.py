from asyncore import loop
from lib2to3.pgen2 import token
from typing import List

def Tokeniser(input: str) -> List[str]:
    tokens = []
    
    for char in input:
        match char:
            case '+':
                tokens.append("INC")
            case '-':
                tokens.append("DEC")
            case '>':
                tokens.append("RGT")
            case '<':
                tokens.append("LFT")
            case '[':
                tokens.append("BOP")
            case ']':
                tokens.append("BCL")
            case '.':
                tokens.append("OUT")
            case ',':
                tokens.append("INP")

    return tokens