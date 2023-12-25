import cv2
import numpy as np

intrinsic = np.array([[1463.2,0,924.5403],[0,1462.6,412.3294],[0,0,1]], dtype=np.double)

distortion = np.array([0.0524,-0.0529, 0, 0],dtype=np.double)

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, f = cam.read()
    if not ret:
        print("无法获取视频帧")
        break
    # get corners
    screen_corners3d = np.array([[145,-135,-40],[-5,-135,-40],[-5,30,-40],[145,30,-40]],dtype=np.double)

    tag_size = 22.2
    image_size = 600
    corner1_3d = np.array([[0,0,0],[tag_size,0,0],[tag_size,tag_size,0],[0,tag_size,0]], dtype=np.double)

    gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
    if gray.shape != (1920, 1080):
        print("WARNING: image shape is not 1920x1080")
    aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)
    params = cv2.aruco.DetectorParameters()
    detector = cv2.aruco.ArucoDetector(aruco_dict, params)
    tag_corners, tag_ids, _ = detector.detectMarkers(gray)
    detected_tag = False
    if tag_ids != None:
        for index, tid in enumerate(tag_ids):
            if tid == 1:
                detected_tag = True
                # print(corner1_3d)
                # print(tag_corners[index])
                _, rvec, tvec = cv2.solvePnP(corner1_3d, tag_corners[index], intrinsic, distortion)
                R, _ = cv2.Rodrigues(rvec)
                point2d, _ = cv2.projectPoints(screen_corners3d, R, tvec, intrinsic, distortion)
                pts1 = point2d.astype(np.float32)
                pts2 = np.array([[0, 0], [0, image_size-1], [image_size-1, image_size-1], [image_size-1, 0]], dtype=np.float32)
                M = cv2.getPerspectiveTransform(pts1, pts2)
                result = cv2.warpPerspective(f, M, (image_size, image_size))
    if detected_tag:
        # corners2d = np.array([[100,100],[300,100],[300,300],[100,300]])
        cv2.polylines(f,[point2d.astype(np.int32)],isClosed=True,color=(255,0,0),thickness=3)
        points2d = np.array([[0,0],[0,599],[599,599],[599,0]])
        M = cv2.getPerspectiveTransform(point2d.astype(np.float32), points2d.astype(np.float32))
        cut = cv2.warpPerspective(f,M,(600,600))
        cv2.imshow("original image", f)
        cv2.imshow("cut result", cut)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()