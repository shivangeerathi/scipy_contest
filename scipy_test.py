# Import data
import time
import numpy as np
import pandas as pd
from skimage import io
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import sys
from ipywidgets import interactive, HBox, VBox, widgets, interact



## loading data
cmd = pd.read_csv('cmd.csv', index_col=0)

### plotting
fig = go.Figure(data=go.Scatter3d(
    x=cmd['color'],
    y=cmd['age'],
    z=cmd['magnitude'],
    mode='markers',
    marker=dict(
        color = cmd['Z'],
        colorscale = 'inferno',
        colorbar_title = 'Metallicity'
    )
))

camera = dict(eye=dict(x=0.5, y=-2., z=0.6))#,up=dict(x=0,y=0.5,z=0.5))

fig.update_layout(scene_camera=camera,
                scene=dict(
                xaxis = dict(title='V-I', range=[-0.75, 2]),
                yaxis = dict(title='Age (Gyrs)', range=[0, 14] ),
                zaxis = dict(title='M<sub>I</sub>', range=[4, -4]),
                aspectmode='cube', #dict(x=1, y=1, z=0.5),
                ),
                height=800, width=800,
                title='Color-magnitude diagram of a simulated galaxy')
                  # zaxis=list(autorange="reversed"))

fig.update_traces(marker=dict(size=3))

### saving figure
fig.write_html("cmd_3D.html")
fig.show()
