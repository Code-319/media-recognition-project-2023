from pymycobot.mycobot import MyCobot
import time
Half_Block_Size=20

mc = MyCobot('COM4',115200)
POS_LIST = {           
    #[x, y, z, rx, ry, rz] 
    "left_front_corner":
        [[215, 48, 230, -180, 0, 0],      # up
        [215, 48, 100, -180, 0, 0]],   # down
         
    "right_front_corner":
        [[215, -59, 230, -180, 0, 0],      # up
        [215, -59, 100, -180, 0, 0]],   # down

    "left_back_corner":
        [[150, 48, 230, -180, 0, 0],      # up
        [150, 48, 100, -180, 0, 0]],   # down
         
    "right_back_corner":
        [[150, -59, 230, -180, 0, 0],      # up
        [150, -59, 100, -180, 0, 0]],   # down
    
    "box_left_back":
        [[120, 170, 240, -180, 0, 0],      # up
        [120, 170, 175, -180, 0, 0]],   # down
    
    "box_left_front":
        [[200, 120, 230, -180, 0,0],      # up
        [215, 150, 220, -150, 0, -60]],   # down
        
    "box_right_back":
        [[120, -150, 240, -180, 0, 0],      # up
        [120, -150, 175, -180, 0, 0]],   # down
    
    "box_right_front":
        [[200, -100, 235, -180, 0,0],      # up
        [220, -140, 220, -150, -10, -80]],   # down
}
MODE = 0


def pump_on():
    mc.set_basic_output(2, 0)
    mc.set_basic_output(5, 0)

def pump_off():
    mc.set_basic_output(2, 1)
    mc.set_basic_output(5, 1)
    
def init():
    mc.send_angles([0, 0, 0, 0, 0, 0], 40) 
    time.sleep(6)

def go(FROM, TO):
    mc.send_coords(FROM, 40, MODE)
    time.sleep(4)
    mc.send_coords(TO, 40, MODE)
    
def grasp(FROM, TO):
    pump_on()
    mc.send_coords(FROM, 40, MODE)
    time.sleep(4)
    mc.send_coords(TO, 40, MODE)
    time.sleep(6)
    mc.send_coords(FROM, 40, MODE)
    time.sleep(2)

def put_off(FROM, TO):
    mc.send_coords(FROM, 40, MODE)
    time.sleep(2)
    mc.send_coords(TO, 40, MODE)
    time.sleep(2)
    pump_off()
    time.sleep(4)
    mc.send_coords(FROM, 40, MODE)
    time.sleep(2)