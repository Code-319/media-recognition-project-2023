import numpy as np

intrinsic = np.array([[1463.2,0,924.5403],[0,1462.6,412.3294],[0,0,1]], dtype=np.double)

distortion = np.array([0.0524,-0.0529, 0, 0],dtype=np.double)

screen_corners3d = np.array([[145,-135,-40],[-5,-135,-40],[-5,30,-40],[145,30,-40]],dtype=np.double)

tag_size = 22.2
image_size = 600
corner1_3d = np.array([[0,0,0],[tag_size,0,0],[tag_size,tag_size,0],[0,tag_size,0]], dtype=np.double)