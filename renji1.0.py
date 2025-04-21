# -*- coding: UTF-8 -*-
import uptech
import signal
import time


RWHEEL = 2
LWHEEL = 1
LFOOT = 4
RFOOT = 3
LSHOULDER = 7
LELBOW = 8
LHAND = 5
RSHOULDER =6
RELBOW =10
RHAND =9

ANGLE=6
DISTANCE_HEAD=5
TURN_SPEED = 350

up = uptech.UpTech()

def init():
    up.CDS_SetAngle(LFOOT, 582, 384)
    up.CDS_SetAngle(RFOOT, 582, 384)
    time.sleep(0.5)
    up.CDS_SetAngle(LHAND, 1023, 384)
    up.CDS_SetAngle(RHAND, 512, 384)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 410, 384)
    up.CDS_SetAngle(RELBOW, 190, 384)
    time.sleep(0.5)
    up.CDS_SetAngle(LSHOULDER, 512, 384)
    up.CDS_SetAngle(RSHOULDER, 850, 384)

def go():
    up.CDS_SetSpeed(RWHEEL, -310)
    up.CDS_SetSpeed(LWHEEL, 310)

def slow():
    up.CDS_SetSpeed(RWHEEL, -290)
    up.CDS_SetSpeed(LWHEEL, 300)

def boost():
    up.CDS_SetSpeed(RWHEEL, -480)
    up.CDS_SetSpeed(LWHEEL, 480)
    time.sleep(0.3)


def boost_back():
    up.CDS_SetSpeed(RWHEEL, 620)
    up.CDS_SetSpeed(LWHEEL, -620)
    time.sleep(0.3)


def back():
    up.CDS_SetSpeed(RWHEEL, 300)
    up.CDS_SetSpeed(LWHEEL, -300)



def left():
    up.CDS_SetSpeed(RWHEEL, -TURN_SPEED)
    up.CDS_SetSpeed(LWHEEL, -TURN_SPEED + 20)


def right():
    up.CDS_SetSpeed(RWHEEL, TURN_SPEED)
    up.CDS_SetSpeed(LWHEEL, TURN_SPEED + 20)


def left_back():
    up.CDS_SetSpeed(RWHEEL, -160)
    up.CDS_SetSpeed(LWHEEL, -390)
    time.sleep(0.4)


def right_back():
    up.CDS_SetSpeed(RWHEEL, 390)
    up.CDS_SetSpeed(LWHEEL, 160)
    time.sleep(0.4)


def stop():
    up.CDS_SetSpeed(RWHEEL, 0)
    up.CDS_SetSpeed(LWHEEL, 0)

#推前方方块
def push_tag():
    # 准备推动
    stop()
    up.CDS_SetAngle(LFOOT, 600, 250)
    up.CDS_SetAngle(RFOOT, 600, 250)
    up.CDS_SetAngle(LELBOW,400,250)
    up.CDS_SetAngle(RELBOW,150,250)
    time.sleep(0.4)
    # 挥动肩膀推下方块
    up.CDS_SetAngle(LSHOULDER, 300, 250)
    up.CDS_SetAngle(RSHOULDER, 650, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 580, 250)
    up.CDS_SetAngle(RELBOW, 280, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(LHAND, 800, 250)
    up.CDS_SetAngle(RHAND, 350, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(LSHOULDER, 150, 500)
    up.CDS_SetAngle(RSHOULDER, 500, 500)
    time.sleep(0.5)
    # 推下完毕，恢复姿态，后退
    up.CDS_SetAngle(LELBOW, 450, 384)
    up.CDS_SetAngle(RELBOW, 100, 384)
    up.CDS_SetAngle(LSHOULDER, 512, 256)
    up.CDS_SetAngle(RSHOULDER, 850, 256)
    time.sleep(0.5)
    up.CDS_SetAngle(LFOOT, 582, 256)
    up.CDS_SetAngle(RFOOT, 582, 256)
    up.CDS_SetAngle(LHAND, 1000, 256)
    up.CDS_SetAngle(RHAND, 512, 256)
    up.CDS_SetAngle(RELBOW, 190, 256)
    time.sleep(1.0)
    back()
    time.sleep(0.5)
    left()
    time.sleep(0.5)
    slow()
    time.sleep(0.5)
    go()
    time.sleep(0.5)

#推右方方块
def push_tag_R():
    stop()
    up.CDS_SetAngle(LFOOT, 600, 250)
    up.CDS_SetAngle(RFOOT, 600, 250)
    up.CDS_SetAngle(RELBOW, 150, 250)
    time.sleep(0.4)
    # 挥动肩膀推下方块
    up.CDS_SetAngle(RSHOULDER, 650, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(RELBOW, 280, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(RHAND, 350, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(RELBOW,80,500)
    time.sleep(0.5)
    # 推下完毕，恢复姿态，后退
    up.CDS_SetAngle(RELBOW, 100, 384)
    up.CDS_SetAngle(RSHOULDER, 850, 256)
    time.sleep(0.5)
    up.CDS_SetAngle(LFOOT, 582, 256)
    up.CDS_SetAngle(RFOOT, 582, 256)
    up.CDS_SetAngle(RHAND, 512, 256)
    up.CDS_SetAngle(RELBOW, 190, 256)
    time.sleep(1.0)
    back()
    time.sleep(0.5)
    left()
    time.sleep(0.5)
    slow()
    time.sleep(0.5)
    go()
    time.sleep(0.5)

#推左方方块
def push_tag_L():
    stop()
    up.CDS_SetAngle(LFOOT, 600, 250)
    up.CDS_SetAngle(RFOOT, 600, 250)
    up.CDS_SetAngle(LELBOW, 400, 250)
    time.sleep(0.4)
    # 挥动肩膀推下方块
    up.CDS_SetAngle(LSHOULDER, 300, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 600, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(LHAND, 800, 250)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW,280,500)
    time.sleep(0.5)
    # 推下完毕，恢复姿态，后退
    up.CDS_SetAngle(LELBOW, 450, 384)
    up.CDS_SetAngle(LSHOULDER, 512, 256)
    time.sleep(0.5)
    up.CDS_SetAngle(LFOOT, 582, 256)
    up.CDS_SetAngle(RFOOT, 582, 256)
    up.CDS_SetAngle(LHAND, 1000, 256)
    time.sleep(1.0)
    back()
    time.sleep(0.5)
    left()
    time.sleep(0.5)
    slow()
    time.sleep(0.5)
    go()
    time.sleep(0.5)

#复位
def recover():
    up.CDS_SetAngle(LFOOT, 582, 384)#大于前倾
    up.CDS_SetAngle(RFOOT, 582, 384)
    up.CDS_SetAngle(LHAND, 1023, 384)#小于往下，大于往上
    up.CDS_SetAngle(RHAND, 512, 384)#小于往下，大于往上
    up.CDS_SetAngle(LELBOW, 410, 384)#小于往外，大于往内
    up.CDS_SetAngle(RELBOW, 190, 384)#小于往外，大于往内
    up.CDS_SetAngle(LSHOULDER, 512, 384) #小与512往前伸，大于往后
    up.CDS_SetAngle(RSHOULDER, 850, 384)#小于往前，大于往后

#攻击1
def attack_1():
   stop()
   up.CDS_SetAngle(LFOOT, 582, 384)
   up.CDS_SetAngle(RFOOT, 582, 384)
   up.CDS_SetAngle(LSHOULDER,250,900)
   up.CDS_SetAngle(RSHOULDER, 580, 900)
   time.sleep(1)
   up.CDS_SetAngle(LELBOW, 550, 800)
   up.CDS_SetAngle(RELBOW, 300, 800)
   time.sleep(1)
   up.CDS_SetAngle(LHAND, 800, 1023)
   up.CDS_SetAngle(RHAND, 290, 1023)
   time.sleep(1)
   # go()
   # time.sleep(0.5)
   recover()
   time.sleep(0.5)

#左手攻击
def attack_L():
    stop()
    up.CDS_SetAngle(LFOOT, 582, 384)
    up.CDS_SetAngle(RFOOT, 582, 384)
    up.CDS_SetAngle(LSHOULDER, 190, 600)
    time.sleep(0.3)
    up.CDS_SetAngle(LELBOW, 750, 600)
    time.sleep(0.3)
    up.CDS_SetAngle(LHAND,800,600)
    time.sleep(0.3)
    up.CDS_SetAngle(LELBOW,250,1000)
    time.sleep(0.3)
    recover()
    time.sleep(0.5)

#右手攻击
def attack_R():
    stop()
    up.CDS_SetAngle(LFOOT, 582, 384)
    up.CDS_SetAngle(RFOOT, 582, 384)
    up.CDS_SetAngle(RSHOULDER, 500, 484)
    time.sleep(0.5)
    up.CDS_SetAngle(RELBOW, 500, 484)
    up.CDS_SetAngle(RHAND, 350, 484)
    time.sleep(0.5)
    up.CDS_SetAngle(RELBOW,80,1000)
    time.sleep(0.5)
    recover()
    time.sleep(0.5)

#后倾前起
def front_stand():
    up.CDS_SetAngle(LSHOULDER,680,500)
    up.CDS_SetAngle(RSHOULDER,1023,500)
    up.CDS_SetAngle(LHAND,900,500)
    up.CDS_SetAngle(RHAND,400,500)
    # up.CDS_SetSpeed(RWHEEL,600)
    # up.CDS_SetSpeed(LWHEEL,600)

#前倾后起
def back_stand():
    up.CDS_SetAngle(RSHOULDER,700,500)
    up.CDS_SetAngle(LSHOULDER,400,500)
    up.CDS_SetSpeed(RWHEEL,1000)
    up.CDS_SetSpeed(LWHEEL,1000)

#登台
def up_platform():
    # 上坡
    up.CDS_SetAngle(LFOOT, 620, 256)
    up.CDS_SetAngle(RFOOT, 620, 256)
    time.sleep(0.1)
    up.CDS_SetSpeed(RWHEEL, -350)
    up.CDS_SetSpeed(LWHEEL, 350)
    time.sleep(1.5)
    # 进入擂台
    up.CDS_SetAngle(LFOOT, 582, 512)
    up.CDS_SetAngle(RFOOT, 582, 512)
    time.sleep(0.5)
    up.CDS_SetSpeed(RWHEEL, -400)
    up.CDS_SetSpeed(LWHEEL, 650)
    time.sleep(1.2)
    go()
    time.sleep(1.5)

#停止行动信号
def signal_handler(signal, frame):
    stop()
    exit(0)

#边缘检测
def edge_detect():
    #1为没检测到，0为检测到
    if zuo_qian_hw==1 and you_qian_hw==1:
        right()
        time.sleep(0.5)
    # while zuo_hou_hw==1 and you_hou_hw==1:
    #     boost()
    elif zuo_qian_hw==1 and you_qian_hw==0:
        right()
        time.sleep(0.7)
    elif zuo_qian_hw==0 and you_qian_hw==1:
        left()
        time.sleep(0.5)


def enemy_detect():
    if adc_data[DISTANCE_HEAD]>429 and adc_data[DISTANCE_HEAD]<920:
        attack_L()
        print('zuo')
        time.sleep(0.2)
        attack_R()
        print('you')
        time.sleep(0.2)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)#停止行动信号
    io_data=[]
    up.ADC_IO_Open()
    up.CDS_Open()
    # adc_data=[]

    up.CDS_SetMode(LWHEEL,1)
    up.CDS_SetMode(RWHEEL, 1)
    up.CDS_SetMode(LFOOT, 0)
    up.CDS_SetMode(RFOOT, 0)
    up.CDS_SetMode(LSHOULDER, 0)
    up.CDS_SetMode(RSHOULDER,0)
    up.CDS_SetMode(LELBOW,0)
    up.CDS_SetMode(RELBOW,0)
    up.CDS_SetMode(LHAND,0)
    up.CDS_SetMode(RHAND,0)

    #无接触启动
    # while True:
    #     adc_data=up.ADC_Get_All_Channle()
    #     if adc_data[DISTANCE_HEAD] > 920:
    #         break
    #
    # up_platform()
    #429手臂最长距离
    while True:
        adc_data=up.ADC_Get_All_Channle()
        #io读取
        io_all_input = up.ADC_IO_GetAllInputLevel()
        io_array = '{:08b}'.format(io_all_input)
        io_arr=io_array.replace('-','')
        io_data=[]
        for index, value in enumerate(io_arr):
            #print(value)
            io = int(value)
            io_data.insert(0, io)
        zuo_qian_hw = io_data[0]
        you_qian_hw = io_data[1]
        zuo_hou_hw = io_data[2]
        you_hou_hw = io_data[3]
        qian_hw=io_data[6]
        zheng_zuo_qian_hw = io_data[5]
        zheng_you_qian_hw = io_data[7]

        # init()
        up.CDS_SetAngle(LFOOT,582,384)
        up.CDS_SetAngle(RFOOT,582,384)
        front_stand()
        # go()
        # up.CDS_SetAngle(LELBOW,410,384)
        # edge_detect()
        #方块检测及推动
        # if adc_data[DISTANCE_HEAD]<429:
        #     if qian_hw==0 :
        #         push_tag()
        #         print('前检测到')
        #         time.sleep(0.5)
        #     elif zheng_you_qian_hw==0:
        #         push_tag()
        #         print('正右前检测到')
        #         time.sleep(0.5)
        #     elif zheng_zuo_qian_hw==0:
        #         push_tag()
        #         print('正左前检测')
        #         time.sleep(0.5)

        #敌人检测
        # enemy_detect()

