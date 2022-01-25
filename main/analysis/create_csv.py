import functools as ft

from main.analysis.AnalysisUtil import AnalysisHelper

# ***** SCRIPT TO CREATE A BIG FLATTENED CSV WITH ALL DATA FOR THE ANALYSIS *****
# *****  !! ONLY EXECUTED ONCE !! *****

LEAGUES = ["bundesliga", "champions_league", "europa_league", "la_liga", "ligue_1", "premier_league", "serie_a"]
YEARS = list(range(2010, 2020 + 1))

dfs = []
for league in LEAGUES:
    for year in YEARS:
        try:
            df = AnalysisHelper.get_fixtures(league, year)
        except ValueError:
            continue
        dfs.append(df)
allFixtures = ft.reduce(AnalysisHelper.append, dfs).reset_index()

allFixtures.to_csv("allFixtures.csv", encoding='utf-8', index=False)
