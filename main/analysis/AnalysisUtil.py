import functools as ft
import json

import pandas as pd


class AnalysisHelper:

    def get_fixtures(self, league, year):
        if not isinstance(league, list):
            return self.__get_fixtures_of_league(self, league, year)
        else:
            return self.__get_fixtures_of_more_leagues(self, league, year)

    @staticmethod
    def __get_fixtures_of_league(self, league, years):
        if not isinstance(years, list):
            with open(f"../resources/{league}/{league}_{years}.json", "r") as read_file:
                data = json.load(read_file)
                df = pd.json_normalize(data['response'][0])
                for response in data['response'][1:]:
                    df1 = pd.json_normalize(response)
                    df = df.append(df1, ignore_index=True)

            return df
        else:
            dfs = []
            for year in years:
                with open(f"../resources/{league}/{league}_{year}.json", "r") as read_file:
                    data = json.load(read_file)
                    df = pd.json_normalize(data['response'][0])
                    for response in data['response'][1:]:
                        df1 = pd.json_normalize(response)
                        df = df.append(df1, ignore_index=True)
                dfs.append(df)

            return ft.reduce(self.__append, dfs).reset_index()

    @staticmethod
    def __get_fixtures_of_more_leagues(self, leagues, years):
        if not isinstance(years, list):
            dfs = []
            for league in leagues:
                with open(f"../resources/{league}/{league}_{years}.json", "r") as read_file:
                    data = json.load(read_file)
                    df = pd.json_normalize(data['response'][0])
                    for response in data['response']:
                        df1 = pd.json_normalize(response)
                        df = df.append(df1, ignore_index=True)
                dfs.append(df)

            return ft.reduce(self.__append, dfs).reset_index()
        else:
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
                dfs.append(df)

            return ft.reduce(self.__append, dfs).reset_index()

    @staticmethod
    def __append(a, b):
        return a.append(b)
