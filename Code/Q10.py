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
            if row['S/R']!='-' :
                row["S/R"]=str(row["S/R"]).replace("*","")
                players[sheet].append(row['S/R'])
players_stats = {
    player: (np.mean([float(i) for i in player_data]), np.var([float(i) for i in player_data]), np.mean([float(i) for i in player_data if float(i) > 0])) 
    for player, player_data in players.items() if player_data
}
sorted_players = sorted(players_stats.items(), key=lambda x: x[1][2])

top_3 = sorted_players[-3:]
bottom_3 = sorted_players[:3]

labels = [player[0] for player in top_3 + bottom_3]
strike_rates = [player[1][2] for player in top_3 + bottom_3]

x = np.arange(len(labels)) 
width = 0.35 

colors = ['red' if player in [p[0] for p in bottom_3] else 'green' if player in [p[0] for p in top_3] else 'blue' for player in labels]

fig, ax = plt.subplots()
rects = ax.bar(x, strike_rates, width, color=colors)

ax.set_xlabel('Player')
ax.set_ylabel('Strike Rate')
ax.set_title('Strike Rates of Players')
ax.set_xticks(x)
ax.set_xticklabels(labels)

fig.tight_layout()

plt.show()