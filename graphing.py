import os
import plotly.plotly as py
import config
from plotly.graph_objs import *

py.sign_in(config.plotly_user, config.plotly_pass)

dates = []
count_dates = []
counts = []
hours = []

with open(os.path.normpath(config.hours_per_day_filename), 'r') as f:
    rows = f.readlines()

# get summary of dates in file
    for line in rows:
        lines = line.strip().split(',')
        dates.append(lines[0])
        hours.append(lines[1])

trace1 = Bar(x=dates,y=hours)

data = Data([trace1])

layout = Layout(
    title = config.plotly_title,
    xaxis=XAxis(
        title='Date',
        autorange=True
    ),
    yaxis=YAxis(
        title='Number of Hours Played',
        autorange=True
    )
)

fig = Figure(data=data, layout=layout)

plot_url = py.plot(fig, filename=config.plotly_title, fileopt='overwrite', auto_open=False)
