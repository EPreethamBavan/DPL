import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
players={}

for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    for sheet in xls.sheet_names:
        dfs= pd.read_excel(xls, sheet_name=sheet)
        for index, row in dfs.iterrows():
            if row['S/R']!='-' :
                row["S/R"]=str(row["S/R"]).replace("*","")
                position = int(row['Posn'])
                if position > 11:
                    continue
                if position not in players:
                    players[position] = {}
                if sheet not in players[position]:
                    players[position][sheet] = []
                players[position][sheet].append(float(row['S/R']))

best_players = {}
for position, player_data in players.items():
    player_avgs = {player: np.mean(strike_rates) for player, strike_rates in player_data.items()}
    best_player = max(player_avgs.items(), key=lambda x: x[1])
    best_players[position] = best_player

sorted_best_players = dict(sorted(best_players.items()))

for position, player in sorted_best_players.items():
    print(f'Position: {position}, Player: {player[0]}, Average Strike Rate: {player[1]}')

plt.figure(figsize=(10, 5))
plt.bar(range(len(sorted_best_players)), [player[1] for player in sorted_best_players.values()], align='center')
plt.xticks(range(len(sorted_best_players)), [str(player[0]) for player in sorted_best_players.values()])
plt.xlabel('Player')
plt.ylabel('Average Strike Rate')
plt.title('Best Average Strike Rate by Position')
plt.show()