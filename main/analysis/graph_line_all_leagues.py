import pandas as pd
import matplotlib.pyplot as plt
import all_enums as ae

df = pd.read_csv('allFixtures.csv')
leagues = [ae.LeagueID.BUNDESLIGA_ID.real,
           ae.LeagueID.PREMIER_LEAGUE_ID.real,
           ae.LeagueID.LA_LIGA_ID.real,
           ae.LeagueID.LIGUE_1_ID.real,
           ae.LeagueID.SERIE_A_ID.real
]

df1 = df.loc[df['league.id'] == leagues[0]]
df2 = df.loc[df['league.id'] == leagues[1]]
df3 = df.loc[df['league.id'] == leagues[2]]
df4 = df.loc[df['league.id'] == leagues[3]]
df5 = df.loc[df['league.id'] == leagues[4]]

df6 = df1.append(df2)
df6 = df6.append(df3)
df6 = df6.append(df4)
df6 = df6.append(df5)

# extract needed columns
s1 = df6.loc[:, 'teams.home.winner']
s2 = df6.loc[:, 'league.season']
s3 = pd.concat([s1, s2], axis=1)

result = []
x = 0
for season in range(2010, 2021):
    s4 = s3.loc[s3['league.season'] == season, 'teams.home.winner']
    hw = s4.value_counts()[True]
    aw = s4.value_counts()[False]
    d = s4.size - hw - aw
    result.append([hw, aw, d])
    # print([hw, aw, d])


data_h = []
data_a = []
data_d = []
for res in result:
    data_h.append(res[0])
    data_a.append(res[1])
    data_d.append(res[2])

df7 = pd.DataFrame({"Home Wins": data_h,
                    "Away Wins": data_a,
                    "Draws": data_d},
                   index=list(range(2010, 2021)))

plt.plot(list(range(2010, 2021)), data_h, color='#fb8603', linewidth=3.0)
plt.plot(list(range(2010, 2021)), data_a, color='#000000', linewidth=3.0)
plt.plot(list(range(2010, 2021)), data_d, color='#9a8878', linewidth=3.0)
plt.xlabel('Years')
plt.ylabel('Number of Matches')
plt.title(f'Match outcome for all National Leagues')
# plt.text(x=2015, y=700, s=str(56))

plt.legend(['Home Win', 'Away Win', 'Draws'])
plt.savefig(f"all_leagues_graphline.png")
# plt.show()
