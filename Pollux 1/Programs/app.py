import os
import assembler_1gen



working_path = os.getcwd()
codes_path = input("Type where is your working space for all assembly files: ") + "\\"  # napr. "D:\DOYA G-1" + "\\" + "codes" + "\\"
mahcine_files = input("Type where is your working space for all machine files: ") + "\\"

run = True
menu = True
coding = False

code = []
machine_code = ""
address = 0

while run:

    while menu:

        print("                                           ================================")
        print("                                              DOYA Programmer enviroment")
        print("                                           ================================ \n")
        print("                                                   1) Write code")
        print("                                                  2) Assembly code")
        print("                                                      3) Exit")

        inp = input()
        if inp == "1":
            coding = True
            menu = False
            print("                                           ================================")
            print("                                                 1) Save assembly code")
            print("                                                      2) Exit")
            print("                                           ================================")
            print("                                                You can write your code")

        elif inp == "2":
            assembly_file = input("Type the file name: ")

            while not os.path.exists(codes_path + assembly_file + ".daf"):  # kontrolujes ci existuje ten assembly file
                assembly_file = input("This file doesn't exist, try again: ")

            with open(os.path.join(codes_path + assembly_file + ".daf"), "r") as file:      # otvaras assembly file a z neho urobis object file
                file_lines = file.readlines()

            with open(os.path.join(mahcine_files + assembly_file + ".dmf"), "w") as object_file:     # tu pises object file

                                                            # - 1
                for line_of_instr in range(0, len(file_lines)):
                    if file_lines[line_of_instr] != "\n":
                        if assembler.assemlby(file_lines[line_of_instr][:-1], address) == None:
                            print(f"Error on line {line_of_instr + 1}")
                            object_file.close()
                # os.remove(os.path.join(mahcine_files + assembly_file + ".dmf"))
                            break

                        if assembler.assemlby(file_lines[line_of_instr][:-1], address)[2] != None:
                            object_file.write("0" * (8 - len(str(assembler.number_in_base(address, 2)))) + str(assembler.number_in_base(address, 2)) + " ")  # preto to je v tomto poradi lebo ja chcem aby adresy pre instrukcie zacinali od nuly
                            address, w, instruction, imm_value = assembler.assemlby(file_lines[line_of_instr][:-1], address)

                            object_file.write(w + " ")
                            object_file.write(instruction + " ")
                            object_file.write(imm_value)
                            object_file.write("\n") if line_of_instr != len(file_lines) - 1 else None

                            print("\nSuccessfully assembled '" + assembly_file + ".daf'" + " into a machine file '" + assembly_file + ".dmf'\n\n") if line_of_instr == len(file_lines) - 2 else None


        elif inp == "3":
            run = False
            menu = False



    while coding:
        line = input()

        if line != "1" and line != "2":
            code.append(line)

        elif line == "1":
            files_name_to_save = input("Name of your file is: ")  # ako sa bude volat subor ktory chces ulozit
            while os.path.exists(codes_path + files_name_to_save + ".daf"):
                files_name_to_save = input("This file already exist, try again: ")

            with open(os.path.join(codes_path + files_name_to_save + ".daf"), "w") as assembly_file: # tu pises assembly file ktory chces ulozit
                for line_num in range(len(code)):
                    assembly_file.write(code[line_num])
                    assembly_file.write("\n") if line_num != len(code) - 1 else None
                code.clear()
                print("\nFile was saved as '" + files_name_to_save + ".daf'\n")

        elif line == "2":
            coding = False
            menu = True
            machine_code = ""
