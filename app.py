from datetime import datetime
import pybaseball
from pybaseball import schedule_and_record, pitching
from pybaseball import statcast
from pybaseball import team_ids
from pybaseball import cache
import pandas as pd
import numpy as np
from pybaseball import schedule_and_record

cache.enable()

### for each game in today's baseball slate,
#teams = team_ids(2024, 'NL')
#todaysGames = schedule_and_record(2024, { teams })


tempTeams = team_ids()
latestTeamsYear = tempTeams['yearID'].max()
teams = team_ids(latestTeamsYear)

for index, row in teams.iterrows():
    #team_name = row['teamName']
    team_id = row['teamIDBR']



    print(f"Team ID: { team_id }")



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