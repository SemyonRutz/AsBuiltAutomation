import pdb, re

def test_calc (path):

    with open (path, 'r') as f:
        test_raw_str = f.read()

    test_str_step1 = test_raw_str.replace("'","")
    test_str_step2 = test_str_step1.replace('"','')

    test_str_list = test_str_step2.split('\n')
    tore_ftg_list = []
    inst_ftg_list = []
    rsr_list = []


    for i in test_str_list:
        cleaned_i_1 = re.sub(' +', ' ', i)
        cleaned_i_2 = cleaned_i_1.strip()

    # checking the installed pipe footage
        if cleaned_i_2[-8:] == 'FITTINGS':
            raw_ftg = cleaned_i_2[11:-14]
            ftg = raw_ftg.replace("," , "")
            inst_ftg_list.append(int(ftg)) 

    # checking the tore pipe footage
        if cleaned_i_2[-6:] == '(TARE)' and cleaned_i_2[2:4] == 'PE':
            raw_ftg = cleaned_i_2[11:-7]
            ftg = raw_ftg.replace("," , "")
            tore_ftg_list.append(int(ftg))

    # checking 1" installed risers
        if cleaned_i_2[:7] == '1 RISER' and  cleaned_i_2[-6:] != '(TARE)':
            rsr = cleaned_i_2[10:11]
            rsr_list.append(int(rsr)*3)

    # checking 2" installed risers
        if cleaned_i_2[:7] == '2 RISER' and cleaned_i_2[-6:] != '(TARE)':
            rsr = cleaned_i_2[10:11]
            rsr_list.append(int(rsr)*2)

    # checking 1" tore risers
        if cleaned_i_2[:7] == '1 RISER' and cleaned_i_2[-6:] == '(TARE)':
            rsr = cleaned_i_2[10:-7]
            rsr_list.append(int(rsr)*3)

    # checking 2" tore risers
        if cleaned_i_2[:7] == '2 RISER' and cleaned_i_2[-6:] == '(TARE)':
            rsr = cleaned_i_2[10:-7]
            rsr_list.append(int(rsr)*2)

    inst_pipe_ftg = sum(inst_ftg_list)
    tore_pipe_ftg = sum(tore_ftg_list)
    rsr_ftg = sum(rsr_list)
    total_footage = inst_pipe_ftg + tore_pipe_ftg + rsr_ftg

    print(f"Total installed pipe footage: {inst_pipe_ftg}")
    print(f"Total tore pipe footage: {tore_pipe_ftg}")
    print(f"Total riser footage: {rsr_ftg}")
    print(f"Total footage: {total_footage}")
# r'C:\Users\srutz\OneDrive - Centuri Group, Inc\As-Built Files 2.0\As-Built Files 2\ex.txt'
path = path = input('Provide a full path: ')
user_input = "not exit"

while user_input != 'exit':
    user_input = input("Press enter to calculate: ")
    test_calc(path)