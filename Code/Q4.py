import pandas as pd
import matplotlib.pyplot as plt 
import math

dismissals={'lbw':0,'b':0,'c':0}
teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    dfs = {}
    for sheet in xls.sheet_names:
        dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)

    for i in dfs:
        a={}
        for index, row in dfs[i].iterrows():
            if row['How Dismissed'] .split()[0]  in ['lbw','b','c']:  
                    dismissals[row['How Dismissed'] .split()[0]]+=1
                          
print(dismissals)

plt.bar(dismissals.keys(), dismissals.values())
plt.xlabel('Modes of Dismissal')
plt.ylabel('Count')
plt.title('Distribution of Dismissals')
plt.show()