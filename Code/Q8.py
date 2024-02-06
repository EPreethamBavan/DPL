import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
players={}

for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    for sheet in xls.sheet_names:
        dfs= pd.read_excel(xls, sheet_name=sheet)
        players[sheet]=[]
        for index, row in dfs.iterrows():
            if row['Runs']!='-':
                row["Runs"]=str(row["Runs"]).replace("*","")
                players[sheet].append(int(row['Runs']))

players_stats = {player: (np.mean(runs), np.std(runs)) for player, runs in players.items() if runs}

sorted_players = sorted(players_stats.items(), key=lambda x: x[1][1])

top_3 = sorted_players[:3]
bottom_3 = sorted_players[-3:]

labels = [player[0] for player in top_3 + bottom_3]
means = [player[1][0] for player in top_3 + bottom_3]
stds = [player[1][1] for player in top_3 + bottom_3]

x = np.arange(len(labels)) 
width = 0.35 

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, means, width, label='Mean')
rects2 = ax.bar(x + width/2, stds, width, label='Std Dev')

ax.set_xlabel('Player')
ax.set_ylabel('Scores')
ax.set_title('Mean and Standard Deviation of Runs by Player')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()