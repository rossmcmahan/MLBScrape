from datetime import datetime
import pybaseball
from pybaseball import schedule_and_record, pitching
from pybaseball import statcast
from pybaseball import team_ids
from pybaseball import cache
import pandas as pd
import numpy as np
from pybaseball import schedule_and_record
from torch.fx.experimental.migrate_gradual_types.constraint_transformation import no_broadcast_dim_with_index

cache.enable()
#test = schedule_and_record(2024, 'SDP')
#test2 = test[test['Date'].str.contains('Thursday, Apr 4')]

### Get today's date
today = datetime.today().strftime('%A, %b %d')

### Get the list of MLB Teams
teams = team_ids(team_ids()['yearID'].max())

### Initialize an empty list to store today's games
todays_games = []

### Loop through each team and get their schedule to populate today's schedule
for index, row in teams.iterrows():
    team_id = row['teamIDBR']
    team_schedule = schedule_and_record(datetime.now().year, team_id)
    team_home_schedule = team_schedule[team_schedule['Home_Away'].str.contains('Home')]
    ### Filter the games for today's schedule
    team_games_today = team_schedule[team_schedule['Date'].str.contains(today, case=False)].iloc[:, : 5]


#    if team_games_today['Home_Away'].eq('Home').any():
#        print("Home")

    ### Add the games to the list if any are found.
    if not team_games_today.empty:
        todays_games.append(team_games_today)

### Convert the list of DataFrames into a single DataFrame
if todays_games:
    todays_games_df = pd.concat(todays_games, ignore_index=True)
else:
    todays_games_df = pd.DataFrame(columns=['Date', 'Opp', 'W/L', 'R', 'RA', 'Inn', 'Rank', 'GB', 'Win', 'Loss', 'Save', 'Time', 'D/N', 'Attendance', 'Streak', 'Orig. Scheduled'])


#    stop=1


#    todaysGames = schedule_and_record(datetime.now().year, team = team_id)[(schedule_and_record(datetime.now().year, team = team_id).Date == f'{ datetime.now().strftime("%A") }, { datetime.now().strftime("%b") } { datetime.today().strftime("%d") }')]

#    yesterdaysResults = statcast(team = team_id)

#    print(f"Team ID: { team_id }")



data = statcast('2024-03-01', '2024-08-15', team='DET')
yesterdayGame = data[(data.game_date == '2024-08-14')]
firstInning = yesterdayGame[(yesterdayGame.inning == 1)]

# statcast_data = pybaseball.statcast_pitcher_expected_stats(2024)
# skstatdf = statcast_data[(statcast_data.player_id == 669373)]
# #print(statcast_data)
#
#
# from pybaseball import pitching_stats
# pitchersdf = pitching_stats(2024)
# skubal = pitchersdf[(pitchersdf.Name == "Tarik Skubal")]
#
# from pybaseball import pitching_stats_range
# pitchingstatrangedf = pitching_stats_range("2024-01-01", "2024-08-14")
# skubalsYear = pitchingstatrangedf[(pitchingstatrangedf.Name == "Tarik Skubal")]
#
# from pybaseball import schedule_and_record
# games = schedule_and_record(2024, "DET")
#
# from pybaseball import team_game_logs
# pitching_logs = team_game_logs(2024, "DET")

print(firstInning)