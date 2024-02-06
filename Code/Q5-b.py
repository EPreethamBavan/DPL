import pandas as pd
import matplotlib.pyplot as plt 
import math
import numpy as np

grounds={}
innings={}
versus={}
teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BOWLERS/{i}_BOWLERS.xlsx')
    dfs = {}
    worst={}
    for sheet in xls.sheet_names:
        dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)
    for j in dfs:
        a={}
        for index, row in dfs[j].iterrows():
            try:
                if row['E/R']!='-':  
                    if row['Ground'] not in grounds: 
                        grounds[row['Ground']]=[float(row['E/R']),1]
                    else:
                        grounds[row['Ground']]=[ grounds[row['Ground']][0]+float(row['E/R']), grounds[row['Ground']][1]+1]
                if row['M/Inns']!='-':
                    if row['M/Inns'] not in innings: 
                        innings[row['M/Inns']]=[float(row['E/R']),1]
                    else:
                        innings[row['M/Inns']]=[ innings[row['M/Inns']][0]+float(row['E/R']), innings[row['M/Inns']][1]+1]
                if row['Versus']!='-':
                    if row['Versus'] not in versus: 
                        versus[row['Versus']]=[float(row['E/R']),1]
                    else:
                        versus[row['Versus']]=[ versus[row['Versus']][0]+float(row['E/R']), versus[row['Versus']][1]+1]                
            except Exception as e:
                pass
res=[];res1=[];res2=[]
for i in grounds:
    res.append(grounds[i][0]/grounds[i][1])
for i in innings:
    res1.append(innings[i][0]/innings[i][1])
for i in versus:
    res2.append(versus[i][0]/versus[i][1])   

res = [value for value in res if not np.isnan(value)]
res1 = [value for value in res1 if not np.isnan(value)]
res2 = [value for value in res2 if not np.isnan(value)]

fig, axs = plt.subplots(3, figsize=(15, 15))


axs[0].boxplot(res)
axs[0].set_title('Boxplot of Average Economy by Grounds')

axs[1].boxplot(res1)
axs[1].set_title('Boxplot of Average Economy by Innings')

axs[2].boxplot(res2)
axs[2].set_title('Boxplot of Average Economy by Versus')

plt.tight_layout()
plt.show()

var_res = np.var(res)
var_res1 = np.var(res1)
var_res2 = np.var(res2)

print(f"Variance of Grounds: {var_res}")
print(f"Variance of Innings: {var_res1}")
print(f"Variance of Versus: {var_res2}")

highest_variance = max(var_res, var_res1, var_res2)
if highest_variance == var_res:
    print("Grounds has the highest variance.")
elif highest_variance == var_res1:
    print("Innings has the highest variance.")
else:
    print("Versus has the highest variance.")

