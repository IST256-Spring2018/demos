# From: https://dev.socrata.com/blog/2016/02/02/plotly-pandas.html

import pandas as pd
import numpy as np
import matplotlib
import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go

cf.go_offline() # required to use plotly offline (no account required).

url = 'https://data.cityofnewyork.us/resource/qiz3-axqb.json?$limit=1000000&\
$where=date%20between%20%272014-01-01T00:00:00%27%20and%20%272015-01-01T00:00:00%27'
collisions = pd.read_json(url)

print(collisions.columns)

contributing_factors = pd.concat(
          [collisions.contributing_factor_vehicle_1,
           collisions.contributing_factor_vehicle_2,
           collisions.contributing_factor_vehicle_3,
           collisions.contributing_factor_vehicle_4,
           collisions.contributing_factor_vehicle_5])

print(contributing_factors)
temp = pd.DataFrame({'contributing_factors':contributing_factors.value_counts()})
df = temp[temp.index != 'Unspecified']
df = df.sort_values(by='contributing_factors', ascending=True)
print(df)
data  = go.Data([
            go.Bar(
              y = df.index,
              x = df.contributing_factors,
              orientation='h'
        )])
layout = go.Layout(
        height = '1000',
        margin=go.Margin(l=300),
        title = "Contributing Factors for Vehicle Collisions in 2015"
)
fig  = go.Figure(data=data, layout=layout)
py.plot(fig)
