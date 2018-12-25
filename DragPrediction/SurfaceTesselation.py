from plyfile import PlyData, PlyElement
import matplotlib.cm as cm
import numpy as np
import plotly.graph_objs as go
import plotly.figure_factory as FF
import plotly.plotly as py
import plotly.io as pio

plydata = PlyData.read('NL Front.ply')

# Read File Header
for element in plydata.elements:
    print(element)
    nr_points=plydata.elements[0].count
    nr_faces=plydata.elements[1].count

# Read the Vertex Coordinates
points=np.array([plydata['vertex'][k] for k in range(nr_points)])
points[0]

x,y,z=zip(*points)

faces=[plydata['face'][k][0] for k in range(nr_faces)]
faces[0]

# Graphical object  

Data3 =FF.create_trisurf(x,y,z, faces, colormap=None, plot_edges=None)

noaxis=dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
          )

fig3 = go.Figure(data=Data3, layout=None)
# fig3['layout'].update(dict(title=title,
#                            width=1000,
#                            height=1000,
#                            scene=dict(xaxis=noaxis,
#                                       yaxis=noaxis,
#                                       zaxis=noaxis,
#                                       aspectratio=dict(x=1, y=1, z=0.4),
#                                       camera=dict(eye=dict(x=1.25, y=1.25, z= 1.25)
#                                      )
#                            )
#                      ))



pio.write_image(fig3, 'fig1.png')