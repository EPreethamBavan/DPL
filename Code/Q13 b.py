import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
players_wickets = {}

for i in teams:
    xls = pd.ExcelFile(f'./Teams/{i}/BOWLERS/{i}_BOWLERS.xlsx')
    try:
        for sheet in xls.sheet_names:
            dfs = pd.read_excel(xls, sheet_name=sheet)
            dfs['Date'] = pd.to_datetime(dfs['Date'])
            dfs = dfs.sort_values('Date')
            dfs['Year'] = dfs['Date'].dt.year
            dfs['Wkts'] = dfs['Wkts'].replace('-', '0').replace('*', '0').astype(float)
            yearly_wickets = dfs.groupby('Year').apply(lambda x: x['Wkts'].iloc[-1] - x['Wkts'].iloc[0])
            players_wickets[sheet] = yearly_wickets.to_dict()
    except :
        pass
    
current_year = pd.to_datetime('today').year
last_5_years = range(current_year - 5, current_year + 1)

player_totals = {}
for player, wkts in players_wickets.items():
    last_5_years_wkts = {year: wickets for year, wickets in wkts.items() if year in last_5_years}
    if last_5_years_wkts:
        total_wickets = sum(last_5_years_wkts.values())
        player_totals[player] = total_wickets

best_player = max(player_totals, key=player_totals.get)
print(f'The purple cap for the next season is expected to be: {best_player}')