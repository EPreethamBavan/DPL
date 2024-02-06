import pandas as pd
import matplotlib.pyplot as plt 
import math
import numpy as np

grounds={}
innings={}
versus={}
teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    dfs = {}
    worst={}
    for sheet in xls.sheet_names:
        dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)
    for i in dfs:
        a={}
        for index, row in dfs[i].iterrows():
            if row['Ground']!='-' and row['Runs'] != '-' and row['S/R'] != '-':  
                row["Runs"]=str(row['Runs']).replace("*","")
                if row['Ground'] not in grounds: 
                    grounds[row['Ground']]=[int(row['Runs'])*0.7+row['S/R']*0.3,1]
                else:
                    grounds[row['Ground']]=[ grounds[row['Ground']][0]+int(row['Runs'])*0.7+row['S/R']*0.3, grounds[row['Ground']][1]+1]
            if row['M/Inns']!='-' and row['Runs'] != '-' and row['S/R'] != '-':  
                row["Runs"]=str(row["Runs"]).replace("*","")
                if row['M/Inns'] not in innings: 
                    innings[row['M/Inns']]=[int(row['Runs'])*0.7+row['S/R']*0.3,1]
                else:
                    innings[row['M/Inns']]=[ innings[row['M/Inns']][0]+int(row['Runs'])*0.7+row['S/R']*0.3, innings[row['M/Inns']][1]+1]
            if row['Versus']!='-' and row['Runs'] != '-' and row['S/R'] != '-':
                row["Runs"]=str(row["Runs"]).replace("*","")
                if row['Versus'] not in versus: 
                    versus[row['Versus']]=[int(row['Runs'])*0.7+row['S/R']*0.3,1]
                else:
                    versus[row['Versus']]=[ versus[row['Versus']][0]+int(row['Runs'])*0.7+row['S/R']*0.3, versus[row['Versus']][1]+1]        
res=[];res1=[];res2=[]
for i in grounds:
    res.append(grounds[i][0]/grounds[i][1])    
for i in innings:
    res1.append(innings[i][0]/innings[i][1]) 
for i in versus:
    res2.append(versus[i][0]/versus[i][1])             

fig, axs = plt.subplots(3, 2, figsize=(15, 15))

axs[0, 0].bar(grounds.keys(), res)
axs[0, 0].set_xlabel('Grounds')
axs[0, 0].set_ylabel('Average Score')
axs[0, 0].set_title('Average Score by Grounds')

axs[1, 0].bar(innings.keys(), res1)
axs[1, 0].set_xlabel('Innings')
axs[1, 0].set_ylabel('Average Score')
axs[1, 0].set_title('Average Score by Innings')

axs[2, 0].bar(versus.keys(), res2)
axs[2, 0].set_xlabel('Versus')
axs[2, 0].set_ylabel('Average Score')
axs[2, 0].set_title('Average Score by Versus')

axs[0, 1].boxplot(res)
axs[0, 1].set_title('Boxplot of Average Score by Grounds')

axs[1, 1].boxplot(res1)
axs[1, 1].set_title('Boxplot of Average Score by Innings')

axs[2, 1].boxplot(res2)
axs[2, 1].set_title('Boxplot of Average Score by Versus')

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

