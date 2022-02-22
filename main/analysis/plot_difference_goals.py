import sys
sys.path.append('../../')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from main.analysis.all_enums import LeagueID

# all_leagues -> all fixtures over all years and leagues
all_leagues = pd.read_csv(f"allFixtures.csv")

# SETUP ALL DATAFRAMES NEEDED
bundesliga = all_leagues.loc[(all_leagues['league.id'] == LeagueID.BUNDESLIGA_ID)].reset_index()
premier_league = all_leagues.loc[(all_leagues['league.id'] == LeagueID.PREMIER_LEAGUE_ID)].reset_index()
serie_a = all_leagues.loc[(all_leagues['league.id'] == LeagueID.SERIE_A_ID)].reset_index()
la_liga = all_leagues.loc[(all_leagues['league.id'] == LeagueID.LA_LIGA_ID)].reset_index()
ligue_1 = all_leagues.loc[(all_leagues['league.id'] == LeagueID.LIGUE_1_ID)].reset_index()

all_national_leagues = pd.concat([bundesliga, premier_league, serie_a, la_liga, ligue_1])

champions_league = all_leagues.loc[(all_leagues['league.id'] == LeagueID.CHAMPIONS_LEAGUE_ID)].reset_index()
europa_league = all_leagues.loc[(all_leagues['league.id'] == LeagueID.EUROPA_LEAGUE_ID)].reset_index()

# CHOOSING DATAFRAME TO BE PLOTTED
LEAGUE_TO_PLOT = all_national_leagues
league_name = 'all_national_leagues'

# START ANALYSIS
league_to_plot_diff = LEAGUE_TO_PLOT.loc[:,
                      ["league.season", "teams.home.id", "teams.away.id", "goals.home", "goals.away"]]
diff_made_home = league_to_plot_diff.loc[:, ['league.season', 'teams.home.id', 'goals.home']]
diff_made_away = league_to_plot_diff.loc[:, ['league.season', 'teams.away.id', 'goals.away']]

grouped_diff_made_home = diff_made_home.groupby(['league.season', 'teams.home.id']).sum().reset_index().rename(
    columns={'teams.home.id': 'teams.id'})
grouped_diff_made_away = diff_made_away.groupby(['league.season', 'teams.away.id']).sum().reset_index().rename(
    columns={'teams.away.id': 'teams.id'})

merged_diff_made = pd.merge(grouped_diff_made_home, grouped_diff_made_away)
merged_diff_made = merged_diff_made.rename(
    columns={'league.season': 'Year', 'goals.home': 'Home Goals', 'goals.away': 'Away Goals'})

merged_diff_made["diff"] = (merged_diff_made["Home Goals"] - merged_diff_made["Away Goals"])

merged_diff_made = merged_diff_made[['Year', 'diff']]

avg_diff_per_year_made = merged_diff_made.groupby(['Year']).mean().reset_index().rename(
    columns={'diff': 'Average Difference in Goals made Home/Away'})

plot = avg_diff_per_year_made.plot(kind='line', x='Year', y='Average Difference in Goals made Home/Away', linewidth=2,
                                   color={'#fb8603'})

x_ticks = np.arange(2010, 2020 + 1, 1)
plt.xticks(x_ticks)
plt.title("Difference in number of Home/Away goals for all National Leagues")
plot.set_ylabel("Number of Goals")
y_ticks = np.arange(2, avg_diff_per_year_made.max()['Average Difference in Goals made Home/Away'], 1)
plt.yticks(y_ticks)

# plot.figure.savefig(f"../visualization/goal_plots/{league_name}.png")
plt.show()
