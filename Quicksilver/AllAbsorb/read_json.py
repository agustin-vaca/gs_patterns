import json
import plotly.express as px
import pandas as pd
import sys

df = pd.read_json("roitrace.00.CollisionEvent.bin.json")
gather = df.get("pattern")[4]
fig = px.histogram(y=gather, 
title="Quicksilver, Histogram func=CollisionEvent, Gather",
log_x=True).update_layout(xaxis_title="count", yaxis_title="accessed cache block index")
fig.update_yaxes(range=[0,50])
fig.write_image("Gather_count_as_x.png")

# for i in range(10):
#     gather = df.get("pattern")[i]
#     fig = px.scatter(x=gather, 
#     title="Quicksilver, func=CollisionEvent, Gather#1",
#     log_y=True).update_layout(xaxis_title="iteration index", yaxis_title="accessed cache block index")
#     fig.update_xaxes(range=[0,50])
#     fig.write_html(f"CollisionEvent_Gather_Scatter{i}.html")



# fig = px.histogram(x=gather_2, 
# title="Quicksilver, func=CollisionEvent, Gather#2",
# log_y=True).update_layout(xaxis_title="iteration index", yaxis_title="accessed cache block index")
# fig.write_html("CollisionEvent_Gather2.html")