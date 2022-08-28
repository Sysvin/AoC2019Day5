# open file and turn string into list of integers
with open('data5.txt', mode='r') as positions:
    input_string = positions.read()
    input_list = input_string.split(',')
    num_list = [int(x) for x in input_list]
    input_id = input("Please Enter An Input Value: ")
    pos = 0

    # main function
    def run_computation():
        global pos
        # work with opcode to add leading zeroes
        inst_val = num_list[pos]
        inst_string = str(inst_val).zfill(4)
        opcode = int(inst_string[2] + inst_string[3])
        all_codes = [1, 2, 3, 4, 5, 6, 7, 8]

        # conditionals to determine opcode, mode and values
        if ((opcode != 99) and (opcode in all_codes)):
            p1 = num_list[pos+1]
            p2 = num_list[pos+2]
            oput = num_list[pos+3]
            if opcode != 3 and opcode != 4:
                if(inst_string[0] == "0"):
                    value2 = int(num_list[p2])
                else:
                    value2 = int(p2)
                if(inst_string[1] == "0"):
                    value1 = int(num_list[p1])
                else:
                    value1 = int(p1)

                if opcode == 1:
                    num_list[oput] = value1 + value2
                    pos += 4
                elif opcode == 2:
                    num_list[oput] = value1 * value2
                    pos += 4
                elif opcode == 5:
                    if value1 != 0:
                        pos = value2
                    else:
                        pos += 3
                elif opcode == 6:
                    if value1 == 0:
                        pos = value2
                    else:
                        pos += 3
                elif opcode == 7:
                    if value1 < value2:
                        num_list[oput] = 1
                    else:
                        num_list[oput] = 0
                    pos += 4
                elif opcode == 8:
                    if value1 == value2:
                        num_list[oput] = 1
                    else:
                        num_list[oput] = 0
                    pos += 4
                else:
                    pos += 1
            else:
                if opcode == 3:
                    if (inst_string[1] == "0"):
                        num_list[p1] = input_id
                    else:
                        num_list[p1] = value1
                    pos += 2
                else:
                    print(num_list[p1])
                    pos += 2
        else:
            if(opcode != 99):
                pos += 1
            else:
                quit()

        run_computation()
    run_computation()
