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
