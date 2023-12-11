import cv2
import numpy as np
from constants import *

class Camera:
    def __init__(self, camera_id = 1):
        self.cam = cv2.VideoCapture(camera_id)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)

    def capture1920x1080(self):
        ret, frame = self.cam.read()
        if ret:
            return frame
        else:
            print("ERROR: capture failed")

    def release(self):
        self.cam.release()

def cut_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if gray.shape != (1920, 1080):
        print("WARNING: image shape is not 1920x1080")

    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)
    params = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, params)

    tag_corners, tag_ids, _ = detector.detectMarkers(gray)

    for index, tid in enumerate(tag_ids):
        if tid == 1:
            # print(corner1_3d)
            # print(tag_corners[index])
            _, rvec, tvec = cv2.solvePnP(corner1_3d, tag_corners[index], intrinsic, distortion)
            R, _ = cv2.Rodrigues(rvec)
            point2d, _ = cv2.projectPoints(screen_corners3d, R, tvec, intrinsic, distortion)
            pts1 = point2d.astype(np.float32)
            pts2 = np.array([[0, 0], [0, image_size-1], [image_size-1, image_size-1], [image_size-1, 0]], dtype=np.float32)
            M = cv2.getPerspectiveTransform(pts1, pts2)
            result = cv2.warpPerspective(img, M, (image_size, image_size))
            result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)

    return result