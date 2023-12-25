import RobarmControl

def move(from_x, from_y, bin_Number):
    # 图片 600 * 600 像素
    # 实际 物块 4*4; 区域 15*15 
    # 拍摄图片 134 * 134 mm^2; 区域 114*114 mm^2
    # 左右修正 10
    # 上下修正 5
    # 对应机械臂参数 (前三列)
    # center
    # x : 150(back) ~ 215(front)
    # y : -59(right) ~ 48(left) 
    # corner
    # x : 135(back) ~ 230(front)
    # y : -74(right) ~ 62(left) 

    x0 = int(-(from_y*134/600)*(230-135)/114)+230
    y0 = int(-(from_x*134/600-10)*(74+62)/114)+62


    POS_FROM = [[x0, y0, 230, -180, 0, 0],
                [x0, y0, 100, -180, 0, 0]]

    RobarmControl.pump_on()
    RobarmControl.init()
    RobarmControl.grasp(POS_FROM[0], POS_FROM[1])

    if bin_Number == 0:
        RobarmControl.put_left_front()
    elif bin_Number == 1:
        RobarmControl.put_left_back()
    elif bin_Number == 2:
        RobarmControl.put_right_front()
    elif bin_Number == 3:
        RobarmControl.put_right_back() 

    RobarmControl.init()

if __name__ == "__main__":
    move(500, 100, 3)















