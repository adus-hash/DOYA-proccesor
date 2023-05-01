from math import *

opcodes = { "HTL": "00000000",
            "ADD":"0001",
            "SUB": "0010",
            "MUL": "0011",
            "AND": "0100",
            "OR": "0101",
            "CMP": "0110",
            "LDR": "0111",
            "STR": "1000",
            "MOV": "1001",
            "NOT": "101000",
            "SHL": "101001",
            "SHR": "101010",
            "NEG": "101011",
            "XOR": "101100",
            "CLS": "101101",
            "INP": "101110",
            "JMP": "101111",
            "JC": "111000",
            "JA": "110100",
            "JE": "110010",
            "JZ": "110001",
            "AX": "00",
            "BX": "01",
            "CX": "10",
            "DX": "11"
}
     # from decimal to any base system
def number_in_base(decimal_num, base):
    if type(decimal_num) == type(6):
        saved_decimal_num = decimal_num
        base_num = ""
        while decimal_num > 0:
            base_num += str(decimal_num - (base * floor(decimal_num / base))) if decimal_num - (base * floor(decimal_num / base)) < 10 else chr(96 + decimal_num - (base * floor(decimal_num / base)) - 9)
            decimal_num = floor(decimal_num / base)
        return base_num[::-1] if saved_decimal_num != 0 else "0"
    else:
        print(f"\n\nnumber_in_base(decimal number musi byt type(int)), recived - {type(decimal_num)}")
        #exit(1)

     # from binary to any base number
def number_in_base_binary(bin_num, base):
    if type(bin_num) == type("bin_num musi byt type(str)"):
        new_num = 0
        for exp in range(len(str(bin_num)) - 1, -1, -1):
            new_num += int(bin_num[len(bin_num) - 1 - exp]) * 2 ** exp

        return number_in_base(new_num, base) if base != 10 else new_num
    else:
        print("Expected binary_num as string not int!")



def not_bin_number(string_num): # flip the bits 0 -> 1 and 1 -> 0
    not_num = ""
    for i in range(len(string_num)):
        not_num += str(abs(int(string_num[i]) - 1))


    return not_num



def assemlby(line, address):
    tokens = []
    for i in line.split(" "):
        tokens.append(i.replace(",", "")) if i != "," and i != "" else None


    opcode = ""
    if len(tokens) == 3 or len(tokens) == 2:
        for token in tokens:
            if len(opcode) < 8:
                opcode += opcodes.get(token.upper()) if token.upper() in opcodes.keys() else ""

            elif "#" in tokens[2]:
                immediate_value = "0" * (8 - len(number_in_base(int(tokens[2][1:]), 2))) + number_in_base(int(tokens[2][1:]), 2) if len(number_in_base(int(tokens[2][1:]), 2)) < 8 else number_in_base(int(tokens[2][1:]), 2)

                return address + 1, "1", opcode, immediate_value if int(tokens[2][1:]) <= 255 else number_in_base(255, 2)

    elif len(tokens) == 1:
        if tokens[0].upper() == "HTL":
            opcode += opcodes.get(tokens[0].upper())

        elif tokens[0].upper() == "CLS":
            opcode += opcodes.get(tokens[0].upper()) + "00"

    return (address + 1, "1", opcode, "00000000") if len(opcode) == 8 else None



#print(assemlby("jmp ax, #13", 0))
#print(number_in_base(129, 16))