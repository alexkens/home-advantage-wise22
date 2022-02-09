import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def f1(df, league_id):
    # create
    s1 = df.loc[df['league.id'] == league_id, 'teams.home.winner']
    s2 = df.loc[df['league.id'] == league_id, 'league.season']
    s3 = pd.concat([s1, s2], axis=1)

    result = []
    for season in range(2014, 2021):
        s4 = s3.loc[s3['league.season'] == season, 'teams.home.winner']
        hw = s4.value_counts()[True]
        aw = s4.value_counts()[False]
        d = s4.size - hw - aw
        result.append([hw, aw, d])
        # print([hw, aw, d])

    return result


def f2(result, league_name):
    data_h = []
    data_a = []
    data_d = []
    for res in result:
        data_h.append(res[0])
        data_a.append(res[1])
        data_d.append(res[2])

    df1 = pd.DataFrame({"Home Wins": data_h,
                        "Away Wins": data_a,
                        "Draws": data_d},
                       index=list(range(2014, 2021)))

    ax = df1.plot(kind='bar', stacked=True, color=['#fb8603', '#9a8878', '#000000'], width=0.9)
    # ax.figure(figsize=(8, 6))
    plt.xlabel('Seasons')
    plt.ylabel('Fixtures')
    plt.title(f'Home Advantage in {league_name}')

    for i in range(0, 7):
        h_per = data_h[i] / (data_h[i] + data_a[i] + data_d[i])
        a_per = data_a[i] / (data_h[i] + data_a[i] + data_d[i])
        d_per = data_d[i] / (data_h[i] + data_a[i] + data_d[i])
        h_per = "{:.0%}".format(h_per)
        a_per = "{:.0%}".format(a_per)
        d_per = "{:.0%}".format(d_per)

        print([h_per, a_per, d_per])

        ax.text(i, data_h[i] - 20, h_per, ha='center', va='center')
        ax.text(i, data_a[i] + data_h[i] - 20, a_per, ha='center', va='center')
        ax.text(i, data_a[i] + data_h[i] + data_d[i] - 20, d_per, ha='center', va='center', color='white')

    ax.figure.savefig(f"../visualization/{league_name}.png")

    # plt.show()


# Main
df = pd.read_csv('allFixtures.csv')

# Bundesliga 78, Premier League 39, Serie A 135, Ligue 1 61, La Liga 140, Champions League 2, Europa League 3
league_id = 78
league_name = df.loc[df['league.id'] == league_id, 'league.name'].values[0]
f2(f1(df, league_id), league_name)

"""
leagues = [78, 39, 135, 61, 140]
for l in leagues:
    league_name = df.loc[df['league.id'] == l, 'league.name'].values[0]
    f2(f1(df, l), league_name)
"""