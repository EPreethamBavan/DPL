import pandas as pd
import matplotlib.pyplot as plt

a={}
teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    dfs = {}
    for sheet in xls.sheet_names:
        dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)

    for i in dfs:
        for index, row in dfs[i].iterrows():
            if row['Posn']!='-':
                row["Runs"]=str(row["Runs"]).replace("*","")
                if row['Posn'] not in a:
                    a[row['Posn']]=[int(row['Runs']),1]
                else:
                    a[row['Posn']]=[ a[row['Posn']][0]+int(row['Runs']), a[row['Posn']][1]+1]

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/ALLROUNDERS/{i}_ALLROUNDERS.xlsx')
    dfs = {}
    for sheet in xls.sheet_names:
        if sheet.split()[-1] =='a':
            dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)
        
    for i in dfs:
        for index, row in dfs[i].iterrows():
            if row['Posn']!='-':
                row["Runs"]=str(row["Runs"]).replace("*","")
                if row['Posn'] not in a:
                    a[row['Posn']]=[int(row['Runs']),1]
                else:
                    a[row['Posn']]=[ a[row['Posn']][0]+int(row['Runs']), a[row['Posn']][1]+1]
order={'top_order':0,'middle_order':0,'lower_order':0}
for i in a:
    if i<=3:
        order['top_order']+=a[i][0]/a[i][1]
    elif i<=6:
        order['middle_order']+=a[i][0]/a[i][1]
    else:
        order['lower_order']+=a[i][0]/a[i][1]
for i in order:
    if i=='top_order':
        order[i]=order[i]/3
    elif i=='middle_order':
        order[i]=order[i]/3 
    else:
        order[i]=order[i]/4       

max_order = max(order, key=order.get)
print(f"The maximum average runs is from the {max_order} with {order[max_order]} runs.")

plt.bar(order.keys(), order.values())
plt.xlabel('Order')
plt.ylabel('Average Runs')
plt.title('Average Runs by Order')
plt.show()