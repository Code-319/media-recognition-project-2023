from pymycobot.mycobot import MyCobot
import time
SPEED = 100

mc = MyCobot('COM4',115200)

MODE = 0

def pump_on():
    mc.set_basic_output(2, 0)
    mc.set_basic_output(5, 0)

def pump_off():
    mc.set_basic_output(2, 1)
    mc.set_basic_output(5, 1)
    
def init():
    mc.send_angles([0, 0, 0, 0, 0, 0], 100) 

    time.sleep(2)

def go(FROM, TO):
    mc.send_coords(FROM, SPEED, MODE)
    time.sleep(3)
    mc.send_coords(TO, SPEED, MODE)
    time.sleep(3)
    
def grasp(FROM, TO):
    mc.send_coords(FROM, SPEED, MODE)
    time.sleep(1)
    mc.send_coords(TO, SPEED, MODE)
    time.sleep(1)
    #mc.send_coords(FROM, SPEED, MODE)
    #time.sleep(1)

def put_left_front():
    mc.send_angles([16.52, -1.23, -21.57, -36.38, 2.54, -100.72],SPEED)
    time.sleep(0.8)
    mc.send_angles([48.42, -15.02, -35.85, -6.15, 7.99, -62.3],SPEED)
    time.sleep(0.8)
    pump_off()
    mc.send_angles([44.03, -38.93, -47.48, 23.94, 1.93, -60.72],SPEED)
    time.sleep(1)
    mc.send_angles([40.07, -36.65, -36.47, -27.42, 3.6, -77.87],SPEED//2)
    time.sleep(1)

def put_left_back():
    mc.send_angles([16.52, -1.23, -21.57, -36.38, 2.54, -100.72],SPEED)
    time.sleep(0.8)
    mc.send_angles([48.42, -15.02, -35.85, -6.15, 7.99, -62.3],SPEED)
    time.sleep(0.8)
    pump_off()
    mc.send_angles([60.55, -34.01, -36.21, -28.47, 14.06, -62.3],SPEED)
    time.sleep(1)
    mc.send_angles([40.07, -36.65, -36.47, -27.42, 3.6, -77.87],SPEED//2)
    time.sleep(1)

def put_right_front():
    mc.send_angles([16.17, -13.62, -59.94, -18.89, 1.31, -99.66],SPEED)
    time.sleep(0.8)
    mc.send_angles([-16.87, -25.04, -22.76, -20.47, -4.13, -50.32],SPEED)
    time.sleep(0.8)
    pump_off()
    mc.send_angles([-15.99, -54.31, -22.76, 5.88, -7.99, -50.02],SPEED)
    time.sleep(1)
    mc.send_angles([-3.42, -28.21, -52.38, -12.48, -1.31, -50.02],SPEED//2)
    time.sleep(1)

def put_right_back():
    mc.send_angles([16.17, -13.62, -59.94, -18.89, 1.31, -99.66],SPEED)
    time.sleep(0.8)
    mc.send_angles([-16.87, -25.04, -22.76, -20.47, -4.13, -50.32],SPEED)
    time.sleep(0.8)
    pump_off()
    mc.send_angles([-25.57, -0.79, -86.66, 1.84, -5.36, -50.88],SPEED)
    time.sleep(1)
    mc.send_angles([-3.42, -28.21, -52.38, -12.48, -1.31, -50.02],SPEED//2)
    time.sleep(1)




