import sys
sys.path.append('../../')

import pandas as pd
import matplotlib.pyplot as plt

from main.analysis.all_enums import LeagueID


def f1(df, league_id, first_season):
    # filter right columns
    s1 = df.loc[df['league.id'] == league_id, 'teams.home.winner']
    s2 = df.loc[df['league.id'] == league_id, 'league.season']
    s3 = pd.concat([s1, s2], axis=1)

    result = []
    for season in range(first_season, 2021):
        s4 = s3.loc[s3['league.season'] == season, 'teams.home.winner']
        hw = s4.value_counts()[True]
        aw = s4.value_counts()[False]
        d = s4.size - hw - aw
        result.append([hw, aw, d])

    return result


def f2(result, league_name, first_season, number_of_seasons):
    data_h = []
    data_a = []
    data_d = []
    for res in result:
        data_h.append(res[0])
        data_a.append(res[1])
        data_d.append(res[2])

    df1 = pd.DataFrame({"Home Wins": data_h,
                        "Draws": data_d,
                        "Away Wins": data_a},
                       index=list(range(first_season, 2021)))

    ax = df1.plot(kind='bar', stacked=True, color=['#fb8603', '#9a8878', '#000000'], width=0.75)
    # ax.figure(figsize=(8, 6))
    plt.xlabel('Seasons')
    plt.ylabel('Matches')
    plt.title(f'Match Outcome in {league_name}')

    for i in range(0, number_of_seasons):
        h_per = data_h[i] / (data_h[i] + data_a[i] + data_d[i])
        a_per = data_a[i] / (data_h[i] + data_a[i] + data_d[i])
        d_per = data_d[i] / (data_h[i] + data_a[i] + data_d[i])
        h_per = "{:.0%}".format(h_per)
        a_per = "{:.0%}".format(a_per)
        d_per = "{:.0%}".format(d_per)

        ax.text(i, data_h[i] - 20, h_per, ha='center', va='center')
        ax.text(i, data_h[i] + data_d[i] - 20, d_per, ha='center', va='center')
        ax.text(i, 240, a_per, ha='center', va='center', color='white')

    # ax.figure.savefig(f"../visualization/barplot_one_league/{league_name}.png")

    plt.show()


if __name__ == "__main__":
    df = pd.read_csv('allFixtures.csv')

    league_name = df.loc[df['league.id'] == LeagueID.BUNDESLIGA_ID, 'league.name'].values[0]
    f2(f1(df, LeagueID.BUNDESLIGA_ID, 2010), league_name, 2010, 11)
