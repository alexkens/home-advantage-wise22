import sys
sys.path.append('../../')

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from main.analysis.AnalysisUtil import AnalysisHelper

# all_leagues -> all fixtures over all years and leagues
all_leagues = pd.read_csv(f"allFixtures.csv")

#### ANALYSIS FOR GAMES MADE AND CONCEDED ####

# CHOOSE YEAR AND LEAGUE FOR ANALYSE
YEAR = 2010
LEAGUE = "Premier League"
league_year = all_leagues.loc[((all_leagues['league.season'] == YEAR) & (all_leagues['league.name'] == LEAGUE))]

# START ANALYSE FOR GOALS MADE AND CONCEDED
league_goals = league_year.loc[:, ["teams.home.id", "teams.away.id", "goals.home", "goals.away"]]

league_goals_made_home = league_goals.loc[:, ['teams.home.id', 'goals.home']]
league_goals_made_away = league_goals.loc[:, ['teams.away.id', 'goals.away']]

league_goals_conceded_home = league_goals.loc[:, ['teams.home.id', 'goals.away']]
league_goals_conceded_away = league_goals.loc[:, ['teams.away.id', 'goals.home']]

grouped_made_home = league_goals_made_home.groupby(['teams.home.id']).sum().reset_index().rename(
    columns={'teams.home.id': 'teams.id'})
grouped_made_away = league_goals_made_away.groupby(['teams.away.id']).sum().reset_index().rename(
    columns={'teams.away.id': 'teams.id'})

grouped_conceded_home = league_goals_conceded_home.groupby(['teams.home.id']).sum().reset_index().rename(
    columns={'teams.home.id': 'teams.id'})
grouped_conceded_away = league_goals_conceded_away.groupby(['teams.away.id']).sum().reset_index().rename(
    columns={'teams.away.id': 'teams.id'})

merged_goals_made = pd.merge(grouped_made_home, grouped_made_away)
merged_goals_made = merged_goals_made.rename(columns={'goals.home': 'Home Goals', 'goals.away': 'Away Goals'})

merged_goals_conceded = pd.merge(grouped_conceded_home, grouped_conceded_away)
merged_goals_conceded = merged_goals_conceded.rename(
    columns={'goals.away': 'Goals conceded home', 'goals.home': 'Goals conceded away'})

# SORT DATAFRAMES
merged_goals_made = merged_goals_made.sort_values(by=["Home Goals"], ascending=False)
merged_goals_conceded = merged_goals_conceded.sort_values(by=["Goals conceded away"], ascending=False)

max_goals_made = merged_goals_made.max()['Home Goals']
max_goals_conceded = merged_goals_conceded.max()['Goals conceded away']

### PLOTTING ###
ax_goals_made = merged_goals_made.plot(kind='bar', x='teams.id', y=['Home Goals', 'Away Goals'], width=0.7,
                                       color={'#fb8603', '#000'})

# GETS LOGOS VIA HTTP REQUEST
AnalysisHelper.place_logos_teams(merged_goals_made, ax_goals_made)

ax_goals_made.set_xticklabels([])
ax_goals_made.set_ylabel("Number of Goals")
ax_goals_made.set_xlabel('')
plt.yticks(np.arange(0, max_goals_made + 5, 5))
plt.title(f'Home/Away Goals made in {LEAGUE.upper()} Season {YEAR}/{YEAR + 1}')

# ax_goals_made.figure.savefig(f"../visualization/goal_plots/goals_made_{LEAGUE}_{YEAR}.png")
plt.show()

ax_goals_conceded = merged_goals_conceded.plot(kind='bar', x='teams.id',
                                               y=['Goals conceded home', 'Goals conceded away'], width=0.7,
                                               color={'#fb8603', '#000'})

# GETS LOGOS VIA HTTP REQUEST
AnalysisHelper.place_logos_teams(merged_goals_conceded, ax_goals_conceded)

ax_goals_conceded.set_xticklabels([])
ax_goals_conceded.set_ylabel("Number of Goals")
ax_goals_conceded.set_xlabel('')
plt.yticks(np.arange(0, max_goals_made + 5, 5))
plt.title(f'Home/Away Goals conceded in {LEAGUE.upper()} Season {YEAR}/{YEAR + 1}')

# ax_goals_conceded.figure.savefig(f"../visualization/goal_plots/goals_conceded_{LEAGUE}_{YEAR}.png")
plt.show()
