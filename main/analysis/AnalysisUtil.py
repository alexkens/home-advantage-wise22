import functools as ft
import json

import pandas as pd


class AnalysisHelper:

    def get_fixtures(self, leagues, years):
        dfs = []

        if (not isinstance(leagues, str)) | (not isinstance(years, str)):
            for league in leagues:
                for year in years:
                    with open(f"../resources/{league}/{league}_{year}.json", "r") as read_file:
                        data = json.load(read_file)
                        df = pd.json_normalize(data['response'][0])
                        for response in data['response'][1:]:
                            df1 = pd.json_normalize(response)
                            df = df.append(df1, ignore_index=True)
                    dfs.append(df)

            return ft.reduce(self.__append, dfs).reset_index()
        else:
            print("Please pass parameters as lists!")

    @staticmethod
    def __append(a, b):
        return a.append(b)


    def number_of_wins_and_percentages(self, league, year):

        df = self.get_fixtures(league, year)
        win_series = pd.Series(df['teams.home.winner'])
        row_size = df.index.size    # number of all fixtures

        home_wins = win_series.value_counts()[True]
        away_wins = win_series.value_counts()[False]
        draws = row_size - (home_wins + away_wins)

        print("Number of all Fixtures: ", row_size)
        print("Home: ", home_wins)
        print("Away: ", away_wins)
        print("Draws: ", draws)

        home_win_percentage_with_draws = home_wins / row_size
        home_win_percentage_without_draws = home_wins / (row_size - draws)

        print("Home Advantage with draws: %.2f %%" % (home_win_percentage_with_draws * 100))
        print("Home Advantage without draws: %.2f %%" % (home_win_percentage_without_draws * 100))