import pandas as pd
import matplotlib.pyplot as plt 

teams = ['CSK', 'DC', 'GT', 'KKR', 'LSG', 'MI', 'PBKS', 'RR', 'RCB', 'SRH']
batsmen_dismissals = {}

for team in teams:
    xls = pd.ExcelFile(f'./Teams/{team}/BATSMEN/{team}_BATSMEN.xlsx')
    dfs = {}
    for sheet in xls.sheet_names:
        dfs[sheet] = pd.read_excel(xls, sheet_name=sheet)

    for batsman, df in dfs.items():
        for index, row in df.iterrows():
            if isinstance(row['How Dismissed'], str):
                bowler = row['How Dismissed'].split(' b ')[-1]
                if bowler not in  ['not out','did not bat','run out']:
                    if batsman not in batsmen_dismissals:
                        batsmen_dismissals[batsman] = {}
                    if bowler not in batsmen_dismissals[batsman]:
                        batsmen_dismissals[batsman][bowler] = 0
                    batsmen_dismissals[batsman][bowler] += 1

for batsman, bowlers in batsmen_dismissals.items():
    worst_bowler = max(bowlers, key=bowlers.get)
    print(f'{batsman} is most frequently dismissed by {worst_bowler}')