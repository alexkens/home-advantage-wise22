import functools as ft
import json

import pandas as pd


class AnalysisHelper:

    def get_fixtures(self, leagues, years):
        dfs = []
        for league in leagues:
            for year in years:
                with open(f"../resources/{league}/{league}_{year}.json", "r") as read_file:
                    data = json.load(read_file)
                    df = pd.json_normalize(data['response'][0])
                    for response in data['response'][1:]:
                        df1 = pd.json_normalize(response)
                        df = df.append(df1, ignore_index=True)
                dfs.append(df)
            # dfs.append(df)

        return ft.reduce(self.__append, dfs).reset_index()

    @staticmethod
    def __append(a, b):
        return a.append(b)


def number_of_wins_and_percentages(league, year):

    analyzer = AnalysisHelper()
    df = analyzer.get_fixtures(league, year)

    win_series = pd.Series(df['teams.home.winner'])

    df2 = pd.DataFrame({'home.win': win_series})
    row_size = df.index.size    # number of all fixtures

    home_wins = 0
    away_wins = 0
    draws = 0
    something_else = 0

    for i in range(row_size):
        if df2['home.win'][i]:
            home_wins += 1
        elif df2['home.win'][i] is False:
            away_wins += 1
        elif df2['home.win'][i] is None:
            draws += 1
        else:
            something_else += 1

    print("Number of all Fixtures: ", row_size)
    print("Home: ", home_wins)
    print("Away: ", away_wins)
    print("Draws: ", draws)
    # print("Something else: ", something_else)

    home_win_percentage_with_draws = home_wins / row_size
    home_win_percentage_without_draws = home_wins / (home_wins + away_wins)

    print("Home Advantage with draws: %.2f %%" % (home_win_percentage_with_draws * 100))
    print("Home Advantage without draws: %.2f %%" % (home_win_percentage_without_draws * 100))
