# Steam Tracker (HTML Scraping)
Steam gameplay hours tracker which captures hours from steam profiles. This is useful in case the player is gaming with 
their profile hidden which broken the previous script.

## What it does

* Scrapes HTML from Steam profile.
* Logs total hours of gameplay for a game.
* Compares against previous days result.
* Plots it on a pretty graph which you can link to, put on a website, etc.

## How to use

You need a plot.ly account for the graphs, signup here: [https://plot.ly/](https://plot.ly/)

Rename the sample-config.py to config.py and edit values.

Set up steam_logging.py and graphing.py to run as a crontab once a day.

`55 23 * * * python /home/user/scripts/steam_logging.py > /dev/null 2>&1`

`58 23 * * * python /home/user/scripts/graphing.py > /dev/null 2>&1`


That's it. If it all works, updated graphs will appear in your plot.ly page.