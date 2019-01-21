from plyfile import PlyData, PlyElement
import matplotlib.cm as cm
import numpy as np
import plotly as plotly
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

data = np.genfromtxt('points.csv', delimiter=',',skip_header=True)
points[0]
print(data)

# Splitting Car Body
# Split y coordinates
Y_F = data[:,1] < 0.7965
yNew_F = data[Y_F,0:4]

#  Split z coordinates
Z_F = yNew_F[:,2] > 0.2332
zNew_F = yNew_F[Z_F,0:4]
X_F = (((zNew_F[:,0] < -4) | (zNew_F[:,2] > 0.6)) | ((zNew_F[:,0] < -4) | (zNew_F[:,2] > 0.6)))
xNew_F = zNew_F[X_F,0:4]

xNew_F,yNew_F,zNew_F=zip(*points)

faces=[plydata['face'][k][0] for k in range(nr_faces)]
faces[0]
saveData = np.savetxt("faces.csv", faces, delimiter=",")

# Graphical object  
Data3 =FF.create_trisurf(xNew_F,yNew_F,zNew_F, faces, colormap=None, plot_edges=None)

noaxis=dict(showbackground=False,
            showline=False,
            zeroline=False,
            showgrid=False,
            showticklabels=False,
            title=''
          )


fig3 = go.Figure(data=Data3, layout=None)
plotly.offline.plot(fig3, filename='testing.html' )

# Save plot
#pio.write_image(fig3, 'fig1.png')