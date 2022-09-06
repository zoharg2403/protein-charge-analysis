import pandas as pd

# load full data file (.xslx)
data = pd.read_excel('Protein sequences with chrage table.xlsx', sheet_name='Protein sequences', header=None)

AA_charge = {'D': -1, 'E': -1, 'K': 1, 'R': 1}

output_dataframe = pd.DataFrame()
for i in range(len(data)):
    prot_charge = data[1][i].count('K') + data[1][i].count('R') - data[1][i].count('E') - data[1][i].count('D')
    output_dataframe = output_dataframe.append({0: data[0][i], 1: prot_charge}, ignore_index=True)

output_dataframe.to_csv('output protein charge.csv', index=0, header=False)
















