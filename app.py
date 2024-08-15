import pybaseball as pyb
from pybaseball import schedule_and_record
from pybaseball import statcast

statcast_data = pyb.statcast_pitcher_expected_stats(2024)

print(statcast_data)