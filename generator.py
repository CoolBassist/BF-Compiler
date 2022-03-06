from fileinput import close
from typing import List

def Generator(input: List[str]) -> str:
    s = ""
    current_index = 0
    open_bracket_index = []
    opened_bracket_index = []
    closed_bracket_index = []
    open_loops = 0
    close_loops = 0

    for token in input:
        match token:
            case "RGT": current_index += 1
            case "LFT": current_index -= 1
            case "BOP":
                open_bracket_index = [open_loops] + open_bracket_index
                open_loops += 1
            case "BCL":
                closed_bracket_index = [close_loops] + closed_bracket_index
                close_loops += 1

    current_index = 0

    inc_value = 0
    changed_value = False

    for token in input:
        if changed_value and token not in ["INC", "DEC"]:
            s += inc(current_index, inc_value)
            changed_value = False
            inc_value = 0
        match token:
            case "RGT": current_index += 1
            case "LFT": current_index -= 1
            case "INC": inc_value += 1; changed_value = True
            case "DEC": inc_value -= 1; changed_value = True
            case "BOP":
                s += open_bracket(current_index, open_bracket_index[0], closed_bracket_index[0])
                opened_bracket_index = [open_bracket_index.pop(0)] + opened_bracket_index 
            case "BCL": s += close_bracket(current_index, opened_bracket_index.pop(0), closed_bracket_index.pop(0));
            case "OUT":
                s += "\tli a7 11\n\tlw a0 " + str(current_index*4) + "(sp)\n\tecall\n"
            case "INP":
                s += "\tli a7 12\n\tsw a0 " + str(current_index*4) + "(sp)\n\tecall\n"

    return s

def inc(current_index: int, value: int) -> str:
    return "\tlw a0 " + str(current_index*4) + "(sp)\n\taddi a0 a0 " + str(value) + "\n\tsw a0 " + str(current_index*4) + "(sp)\n"

def dec(current_index: int) -> str:
    return "\tlw a0 " + str(current_index*4) + "(sp)\n\taddi a0 a0 -1\n\tsw a0 " + str(current_index*4) + "(sp)\n"

def open_bracket(current_index: int, open_loop: int, close_loop: int) -> str:
    s = "\tlw a0 " + str(current_index*4) + "(sp)\n"
    s += "\tbeqz a0 close_loop" + str(close_loop) + "\n"
    s += "open_loop" + str(open_loop) + ":\n"

    return s

def close_bracket(current_index: int, open_loop: int, close_loop: int) -> str:
    s = "\tlw a0 " + str(current_index*4) + "(sp)\n"
    s += "\tbnez a0 open_loop" + str(open_loop) + "\n"
    s += "close_loop" + str(close_loop) + ":\n"

    return s
