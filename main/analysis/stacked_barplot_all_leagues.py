import sys
sys.path.append('../../')

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from main.analysis.all_enums import LeagueID

# this file contains two plots: 1. "mean win rate over all leagues" from the progress presentation and
# 2. "Match outcome for all National Leagues" from the final presentation

df = pd.read_csv("allFixtures.csv")
df = df.loc[
    ((df['league.id'] != LeagueID.CHAMPIONS_LEAGUE_ID) & (df['league.id'] != LeagueID.EUROPA_LEAGUE_ID))].reset_index()
all_national_games = df.loc[:, ["league.name", "league.season", "teams.home.winner"]]

# if a game is a draw the entry is a NaN, to further work with that the following command transforms all NaN Values to 0
result = all_national_games.fillna(value=0)

# adjust dataframe so that it is not divided by leagues only by seasons
no_league = result.loc[:, ["league.season", "teams.home.winner"]]
no_league_wins = no_league.groupby(["league.season"]).sum().reset_index().rename(columns={"teams.home.winner": "wins"})
no_league_games = no_league.groupby(["league.season"]).count().reset_index().rename(
    columns={"teams.home.winner": "games"})
no_league_help = no_league_wins.merge(no_league_games)
no_league_help["winrate"] = no_league_help["wins"] / no_league_help["games"] * 100

# Plot 1: "Mean win rate over all Leagues"
plt.figure()
sns.barplot(x='league.season', y='winrate', data=no_league_help, color='#fb8603')
plt.title('Mean win rate over all Leagues')
plt.ylim([30, 55])
sns.despine()
plt.axhline(y=no_league_help.winrate.mean(), color='black')
# plt.savefig('../visualization/mean_win_rate/win_rates_mean.png')
plt.show()

# here starts the code for the stacked bar plot from the final presentation for all national leagues


# to calculate the draws we need another value than 0
result_two = all_national_games.fillna(value=-1)

# test returns list of -1, 0, 1 values ( draws, loss, wins)
test = list(map(int, result_two["teams.home.winner"]))
test_df = pd.DataFrame(test, columns=['win_int'])
# attach to dataframe again
result_two['win_int'] = test_df
stacked_bar = result_two.loc[:, ["league.season", "teams.home.winner", "win_int"]] \
    .groupby(["league.season", "teams.home.winner"]).count().reset_index()
# merge with number of all games for all seasons
stacked_bar = stacked_bar.merge(no_league_games)
stacked_bar["rate"] = stacked_bar["win_int"] / stacked_bar["games"] * 100
# dataframe needs to be transformed into wide format
pivot2 = stacked_bar.pivot(index='league.season', columns='teams.home.winner', values='win_int').rename(
    columns={-1: "Draw", False: "Away Win", True: "Home Win"})
draws2 = list(pivot2["Draw"])
wins2 = list(pivot2["Home Win"])
loss2 = list(pivot2["Away Win"])
data_frame2 = pd.DataFrame({'Home Win': wins2, 'Draw': draws2, 'Away Win': loss2}, index=list(range(2010, 2021)))

# Plot 2: "Match outcome for all National Leagues"
ax = data_frame2.plot(kind='bar', stacked=True, color=['#fb8603', '#9a8878', 'black'], width=0.7)
plt.xlabel('Years')
plt.ylabel('Number of Matches')
plt.title('Match outcome for all National Leagues')
plt.xticks(rotation=25)
sns.despine()
# insert percentages inside bars
for i in range(0, 11):
    w_per = wins2[i] / (wins2[i] + loss2[i] + draws2[i])
    l_per = loss2[i] / (wins2[i] + loss2[i] + draws2[i])
    d_per = draws2[i] / (wins2[i] + loss2[i] + draws2[i])
    w_per = "{:.0%}".format(w_per)
    l_per = "{:.0%}".format(l_per)
    d_per = "{:.0%}".format(d_per)

    ax.text(i, wins2[i] - 100, w_per, ha='center', va='center')
    ax.text(i, draws2[i] + wins2[i] - 100, d_per, ha='center', va='center')
    ax.text(i, loss2[i] + draws2[i] + wins2[i] - 400, l_per, ha='center', va='center', color='white')
# plt.savefig('../visualization/match_outcomes_all_leagues/stacked_bar_chart_games.png')
plt.show()
