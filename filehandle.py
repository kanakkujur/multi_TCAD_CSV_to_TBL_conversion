
import pandas as pd
import glob as glob

pl = float(input("enter the positive limit\n"))
nl = float(input("enter the negative limit\n"))
steps = float(input("enter the step value\n"))
deffun = int(input("enter the function type idvg = 0 and cgg = 1 \n"))
max_row = ((pl-nl)/steps)+1
print(max_row)
if (deffun==1): #cgg characteristics
    data = {
        "Gate Voltage": [],
        "Drain Voltage": [],
        "C Gate>Drain": [],
        "C Gate>Source": []
    }
    data1 = {
        "Gate Voltage": [' '],
        "Drain Voltage": [' '],
        "C Gate>Drain": [' '],
        "C Gate>Source": [' ']
    }
    d_eqv = pd.DataFrame(data)
    d_space = pd.DataFrame(data1)

    file_size = []
    path = input("enter the directory path\n")
    name = input("enter the common name of the files for eg; ac_(-1.2)1.csv where name:ac_ only\n")
    files = glob.glob(path+"\\"+'*.csv')
    x = len(files)
    print(x)

    i = nl
    while (i > (nl-0.05) and i < (pl+0.05)):
        y = float(round(i, 2))

        data = pd.read_csv(path+"\\"+f'{name}({y})1.csv', index_col=False, header=0)
        df1 = pd.DataFrame(data)
        file_size = df1.shape
        row = file_size[0]
        col = file_size[1]
        df_vg = df1.loc[row - max_row:row, ['Gate Voltage', 'Drain Voltage', 'C Gate>Drain', 'C Gate>Source']]
        d_eqv = pd.concat([d_eqv, df_vg], ignore_index=True)
        d_eqv = pd.concat([d_eqv, d_space], ignore_index=True)
        print(f'process value({y}) completed')
        i = i + steps

    d_eqv.to_csv(path+"\\"+'cgg.tbl', sep='\t', index=False)

    # CGS AND CGD FILE GENERATION

    d_cgd = d_eqv.loc[:, ['Gate Voltage', 'Drain Voltage', 'C Gate>Drain']]
    d_cgs = d_eqv.loc[:, ['Gate Voltage', 'Drain Voltage', 'C Gate>Source']]

    d_cgd.to_csv(path+"\\"+'cgd.tbl', sep='\t', index=False)
    d_cgs.to_csv(path+"\\"+'cgs.tbl', sep='\t', index=False)
    file_names = d_eqv.shape
    print(d_eqv.shape)
else:   #idvg characteristics
    data = {
        "Gate Voltage": [],
        "Drain Voltage": [],
        "Drain Current": []
    }
    data1 = {
        "Gate Voltage": [' '],
        "Drain Voltage": [' '],
        "Drain Current": [' ']
    }
    d_eqv = pd.DataFrame(data)
    d_space = pd.DataFrame(data1)

    file_size = []
    path = input("enter the directory path\n")
    name = input("enter the common name of the files for eg; ac_(-1.2)1.csv where name:ac_ only\n")
    files = glob.glob(path + '*.csv')
    x = len(files)
    print(x)

    i = nl
    while (i > (nl-0.05) and i < (pl+0.05)):
        y = float(round(i, 2))

        data = pd.read_csv(path+"\\"+f'{name}({y})1.csv', index_col=False, header=0)
        df1 = pd.DataFrame(data)
        file_size = df1.shape
        row = file_size[0]
        col = file_size[1]
        df_vg = df1.loc[row - max_row:row, ['Gate Voltage', 'Drain Voltage', 'Drain Current']]
        d_eqv = pd.concat([d_eqv, df_vg], ignore_index=True)
        d_eqv = pd.concat([d_eqv, d_space], ignore_index=True)
        print(f'process value({y}) completed')
        i = i + steps

    d_eqv.to_csv(path+"\\"+'idvg_raw.tbl', sep='\t', index=False)

    temp_idvg = d_eqv.loc[:, ['Gate Voltage', 'Drain Voltage', 'Drain Current']]
    d_idvg = temp_idvg.reindex(['Drain Voltage', 'Gate Voltage', 'Drain Current'], axis="columns")
    d_idvg.to_csv(path + "\\" + 'idvg.tbl', sep='\t', index=False)

    file_names = d_eqv.shape
    print(d_eqv.shape)