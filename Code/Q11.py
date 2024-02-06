import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
players={}

players_1st_innings = {}
players_2nd_innings = {}

for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    for sheet in xls.sheet_names:
        dfs= pd.read_excel(xls, sheet_name=sheet)
        players_1st_innings[sheet] = []
        players_2nd_innings[sheet] = []
        for index, row in dfs.iterrows():
            if row['S/R']!='-' :
                row["S/R"]=str(row["S/R"]).replace("*","")
                if row['Innings'] == 1:
                    players_1st_innings[sheet].append(row['S/R'])
                elif row['Innings'] == 2:
                    players_2nd_innings[sheet].append(row['S/R'])

players_stats_1st_innings = {player: np.mean([float(i) for i in player_data]) for player, player_data in players_1st_innings.items() if player_data}
players_stats_2nd_innings = {player: np.mean([float(i) for i in player_data]) for player, player_data in players_2nd_innings.items() if player_data}

fig, ax = plt.subplots()
ax.plot(players_stats_1st_innings.keys(), players_stats_1st_innings.values(), label='1st Innings')
ax.plot(players_stats_2nd_innings.keys(), players_stats_2nd_innings.values(), label='2nd Innings')

ax.set_xlabel('Player')
ax.set_ylabel('Average Strike Rate')
ax.set_title('Average Strike Rates of Players in the 1st and 2nd Innings')
ax.legend()

plt.show()