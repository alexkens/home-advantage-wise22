import json
import urllib.request

import pandas as pd
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


class AnalysisHelper:

    # RETURNS DATAFRAME FOR GIVEN LEAGUE AND YEAR
    @staticmethod
    def get_fixtures(league, year):

        with open(f"../resources/{league}/{league}_{year}.json", "r") as read_file:
            data = json.load(read_file)
            try:
                df = pd.json_normalize(data['response'][0])
            except IndexError:
                raise ValueError("THERE IS NO INFORMATION ON GIVEN LEAGUE AND SEASON")
            for response in data['response'][1:]:
                df1 = pd.json_normalize(response)
                df = df.append(df1, ignore_index=True)
        return df

    @staticmethod
    def append(a, b):
        return a.append(b)

    @staticmethod
    def place_logos_teams(df, ax):
        for i, j in enumerate(df['teams.id'].tolist()):
            img = AnalysisHelper.__get_logo_from_team(j)
            im = OffsetImage(img, zoom=0.1)
            im.image.axes = ax

            ab = AnnotationBbox(im, (i, 0), xybox=(0., -16.), frameon=False,
                                xycoords='data', boxcoords="offset points", pad=0)

            ax.add_artist(ab)

    @staticmethod
    def place_logos_leagues(df, ax):
        for i, j in enumerate(df['league.id'].tolist()):
            img = AnalysisHelper.__get_logo_from_league(j)
            im = OffsetImage(img, zoom=0.1)
            im.image.axes = ax

            ab = AnnotationBbox(im, (i, 0), xybox=(0., -16.), frameon=False,
                                xycoords='data', boxcoords="offset points", pad=0)

            ax.add_artist(ab)

    @staticmethod
    def __get_logo_from_team(team_id):
        urllib.request.urlretrieve(
            f'https://media.api-sports.io/football/teams/{team_id}.png',
            "team_logo.png")
        img = Image.open("team_logo.png")
        return img

    @staticmethod
    def __get_logo_from_league(league_id):
        urllib.request.urlretrieve(
            f'https://media.api-sports.io/football/leagues/{league_id}.png',
            "league_logo.png")
        img = Image.open("league_logo.png")
        return img
