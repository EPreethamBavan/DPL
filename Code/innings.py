import os
import pandas as pd
from pathlib import Path

def read_excel_data(file_path, sheet_name):
    if file_path.exists():
        try:
            return pd.read_excel(file_path, sheet_name)
        except pd.errors.ImproperlyConfigured as e:
            print(f"Error reading sheet '{sheet_name}': {e}")
            return None
    else:
        return None

def clean_and_impute(df):
    df_cleaned = df.dropna(axis=1, how='all')

    return df_cleaned

def process_data(folder_path):
    for team_folder in os.listdir(folder_path):
        team_path = Path(folder_path) / team_folder
        if os.path.isdir(team_path):
            batsmen_folder = team_path / "batsmen"
            bowlers_folder = team_path / "bowler"
            allrounders_folder = team_path / "allrounder"

            for batsman_file in os.listdir(batsmen_folder):
                batsman_name = batsman_file.split('.')[0]
                sheet_name = batsman_name
                df = read_excel_data(batsmen_folder / batsman_file, sheet_name)
                if df is not None:
                    df_cleaned = clean_and_impute(df)
                    print(f"Processed Batsman Data: {team_folder} - {batsman_name}")

            for bowler_file in os.listdir(bowlers_folder):
                bowler_name = bowler_file.split('.')[0]
                sheet_name = bowler_name
                df = read_excel_data(bowlers_folder / bowler_file, sheet_name)
                if df is not None:
                    df_cleaned = clean_and_impute(df)
                    print(f"Processed Bowler Data: {team_folder} - {bowler_name}")

            # Process All-Rounders
            for allrounder_file in os.listdir(allrounders_folder):
                allrounder_name = allrounder_file.split('.')[0]
                if "_a" in allrounder_file:
                    sheet_name = f"{allrounder_name} a"
                    df_batting = read_excel_data(allrounders_folder / allrounder_file, sheet_name)
                    if df_batting is not None:
                        df_cleaned_batting = clean_and_impute(df_batting)
                        print(f"Processed All-Rounder Batting Data: {team_folder} - {allrounder_name}")

                elif "_b" in allrounder_file:
                    sheet_name = f"{allrounder_name} b"
                    df_bowling = read_excel_data(allrounders_folder / allrounder_file, sheet_name)
                    if df_bowling is not None:
                        df_cleaned_bowling = clean_and_impute(df_bowling)
                        print(f"Processed All-Rounder Bowling Data: {team_folder} - {allrounder_name}")

data_folder_path = "./Teams"
process_data(data_folder_path)
