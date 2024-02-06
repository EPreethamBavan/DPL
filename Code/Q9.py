import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
players={}

for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    for sheet in xls.sheet_names:
        dfs= pd.read_excel(xls, sheet_name=sheet)
        players[sheet]={"top_order":[[],[]],"middle_order":[[],[]],"lower_order":[[],[]]}
        for index, row in dfs.iterrows():
            if row['Runs']!='-' and row['Posn']!='-' and row['S/R']!='-':
                row["Runs"]=str(row["Runs"]).replace("*","")
                if row['Posn']<=3:
                    players[sheet]['top_order'][0].append(int(row['Runs']))
                    players[sheet]['top_order'][1].append(float(row['S/R']))
                elif row['Posn']<=6:
                    players[sheet]['middle_order'][0].append(int(row['Runs']))
                    players[sheet]['middle_order'][1].append(float(row['S/R']))
                else:
                    players[sheet]['lower_order'][0].append(int(row['Runs']))
                    players[sheet]['lower_order'][1].append(float(row['S/R']))

players_var_runs = {
    player: np.var([np.mean([float(i) for i in player_data[pos][0]]) for pos in ['top_order', 'middle_order', 'lower_order'] if player_data[pos][0]]) 
    for player, player_data in players.items() if sum(len(player_data[pos][0]) > 0 for pos in ['top_order', 'middle_order', 'lower_order']) >= 2
}
players_var_sr = {
    player: np.var([np.mean([float(i) for i in player_data[pos][1]]) for pos in ['top_order', 'middle_order', 'lower_order'] if player_data[pos][1]]) 
    for player, player_data in players.items() if sum(len(player_data[pos][1]) > 0 for pos in ['top_order', 'middle_order', 'lower_order']) >= 2
}

sorted_players_runs = sorted(players_var_runs.items(), key=lambda x: x[1])
sorted_players_sr = sorted(players_var_sr.items(), key=lambda x: x[1])

top_3_runs = sorted_players_runs[-3:]
bottom_3_runs = sorted_players_runs[:3]
top_3_sr = sorted_players_sr[-3:]
bottom_3_sr = sorted_players_sr[:3]

players_avg_runs = {
    player: {
        position: np.mean([float(i) for i in data[0]]) 
        for position, data in player_data.items() if data[0]
    } 
    for player, player_data in players.items() if player in [p[0] for p in top_3_runs + bottom_3_runs]
}
players_avg_sr = {
    player: {
        position: np.mean([float(i) for i in data[1]]) 
        for position, data in player_data.items() if data[1]
    } 
    for player, player_data in players.items() if player in [p[0] for p in top_3_sr + bottom_3_sr]
}

fig, ax = plt.subplots(figsize=(10, 6))

for player, player_data in players_avg_runs.items():
    positions = list(player_data.keys())
    avg_runs = [data for data in player_data.values()]
    ax.plot(positions, avg_runs, marker='o', label=player)
    if player in [p[0] for p in top_3_runs]:
        ax.text(positions[-1], avg_runs[-1], f'{player} (Top 3)', horizontalalignment='right')
    elif player in [p[0] for p in bottom_3_runs]:
        ax.text(positions[-1], avg_runs[-1], f'{player} (Bottom 3)', horizontalalignment='right')

ax.set_xlabel('Batting Order')
ax.set_ylabel('Average Runs')
ax.set_title('Average Runs for Top 3 and Bottom 3 Players Across Different Batting Orders')
ax.legend()

plt.show()

fig, ax = plt.subplots(figsize=(10, 6))

for player, player_data in players_avg_sr.items():
    positions = list(player_data.keys())
    avg_sr = [data for data in player_data.values()]
    ax.plot(positions, avg_sr, marker='o', label=player)
    if player in [p[0] for p in top_3_sr]:
        ax.text(positions[-1], avg_sr[-1], f'{player} (Top 3)', horizontalalignment='right')
    elif player in [p[0] for p in bottom_3_sr]:
        ax.text(positions[-1], avg_sr[-1], f'{player} (Bottom 3)', horizontalalignment='right')

ax.set_xlabel('Batting Order')
ax.set_ylabel('Average Strike Rate')
ax.set_title('Average Strike Rates for Top 3 and Bottom 3 Players Across Different Batting Orders')
ax.legend()

plt.show()