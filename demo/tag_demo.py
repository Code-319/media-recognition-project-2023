import cv2
import numpy as np

cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

while True:
    ret, f = cam.read()
    if not ret:
        print("无法获取视频帧")
        break
    # get corners
    corners2d = np.array([[100,100],[300,100],[300,300],[100,300]])
    cv2.polylines(f,[corners2d.astype(np.int32)],isClosed=True,color=(255,0,0),thickness=3)
    points2d = np.array([[0,0],[0,599],[599,599],[599,0]])
    M = cv2.getPerspectiveTransform(corners2d.astype(np.float32), points2d.astype(np.float32))
    cut = cv2.warpPerspective(f,M,(600,600))
    cv2.imshow("original image", f)
    cv2.imshow("cut result", cut)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()