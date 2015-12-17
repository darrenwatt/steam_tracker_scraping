# -*- coding: utf-8 -*-
import os
import time
import requests
import config
from bs4 import BeautifulSoup

steamid = config.steamids
game_title = config.game_title
hrs_daily = config.hours_per_day_filename
hrs_total = config.hours_cumulative_filename


def get_hours_from_profile():
    base_url = "http://steamcommunity.com/id/" + steamid
    r = requests.get(base_url)
    print "Parsing response..."
    soup = BeautifulSoup(r.text, "html.parser")
    games = soup.find('div', class_='recent_games')

    for game in games.contents:
        content = unicode(game)
        if game_title.decode('utf8') in content:
            path_list = content.split()
            hours = path_list.index("hrs")
            player_hours = path_list[hours-1].replace(",","")
    return player_hours


def log_cumulative(logged_hours):
    print "Logging cumulative hours..."
    timestamp = time.strftime('%m/%d/%Y')
    write_status = "{0}, {1}\n".format(timestamp, logged_hours)
    with open(os.path.normpath(hrs_total), "a") as f:
        f.write(write_status)
    print "Cumulative hours logged ({}).".format(logged_hours)


def log_diff():
    print "Logging daily gameplay hours..."
    # get last 2 values from logged_hours
    with open(os.path.normpath(hrs_total), "r") as f:
        lines = f.read().splitlines()
    # diff them
    if len(lines) > 1:
        yesterdays_hours = int(lines[-1].split(',')[1])
        day_before_that_hours = int(lines[-2].split(',')[1])
        diff = (yesterdays_hours - day_before_that_hours)
        # write to file
        timestamp = time.strftime('%m/%d/%Y')
        write_status = "{0}, {1}\n".format(timestamp, diff)
        with open(os.path.normpath(hrs_daily), "a") as f:
            f.write(write_status)
        print "Daily gameplay hours logged ({}).".format(diff)
    else:
        print "Seems to be the first record, no comparison possible."

today_hours = get_hours_from_profile()
log_cumulative(today_hours)
log_diff()

print "Done."
