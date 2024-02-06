import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
players_runs = {}

for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BATSMEN/{i}_BATSMEN.xlsx')
    for sheet in xls.sheet_names:
        dfs = pd.read_excel(xls, sheet_name=sheet)
        for index, row in dfs.iterrows():
            if row['Runs'] != '-':
                date = pd.to_datetime(row['Date'])
                year = date.year
                runs = float(str(row['Runs']).replace('*', ''))
                if sheet not in players_runs:
                    players_runs[sheet] = {}
                period = year // 5
                if period not in players_runs[sheet]:
                    players_runs[sheet][period] = []
                players_runs[sheet][period].append(runs)

player_predictions = {}
for player, runs in players_runs.items():
    X = np.array(list(runs.keys())).reshape(-1, 1) * 5
    y = np.array([np.mean(r) for r in runs.values()]).reshape(-1, 1)
    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, y.ravel())
    next_period = max(runs.keys()) + 1
    player_predictions[player] = model.predict([[next_period * 5]])[0]

best_player = max(player_predictions, key=player_predictions.get)
print(f'Theorange cap for the next season is expected to be: {best_player}')

predicted_runs_per_match = player_predictions[best_player]
predicted_total_runs = predicted_runs_per_match * 14
print(f'The predicted total runs {best_player} is: {predicted_total_runs}')

