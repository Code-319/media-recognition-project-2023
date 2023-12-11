import numpy as np

intrinsic = np.array([[1440.9,0,918.2707],[0,1442.6,421.1895],[0,0,1]], dtype=np.double)

distortion = np.array([0.0282,-0.0314, 0, 0],dtype=np.double)

screen_corners3d = np.array([[150,-135,-40],[0,-135,-40],[0,35,-40],[150,35,-40]],dtype=np.double)

tag_size = 22.2
image_size = 600
corner1_3d = np.array([[0,0,0],[tag_size,0,0],[tag_size,tag_size,0],[0,tag_size,0]], dtype=np.double)