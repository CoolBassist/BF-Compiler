from typing import List

def Parser(input: List[str]) -> str:
    open_loops = 0
    current_index = 0

    for token in input:
        match token:
            case 'RGT':
                current_index += 1
                if current_index >= 3000:
                    return "Accessing unaccessible higher bound memory"
            case 'LFT':
                current_index -= 1
                if current_index < 0:
                    return "Accessing unaccessible lower bound memory"
            case 'BOP':
                open_loops += 1
            case 'BCL':
                open_loops -= 1
                if open_loops < 0:
                    return "Unmatched closed bracket"
    
    if open_loops != 0:
        return "Unmatched open bracket"
    
    return "OK"