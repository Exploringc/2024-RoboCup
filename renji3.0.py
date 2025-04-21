# -*- coding: UTF-8 -*-
import uptech
import signal
import time
import apriltag
import cv2
import numpy as np
from pid import pid


class Atag:
    def __init__(self):
        self.options = apriltag.DetectorOptions(families="tag36h11")
        self.detector = apriltag.Detector(self.options)

    def detect(self, gray):
        return self.detector.detect(gray)

    def get_distance(self, H, t):
        """
        :param H: homography matrix
        :param t: ???
        :return: distance
        """
        ss = 0.5
        src = np.array([[-ss, -ss, 0],
                        [ss, -ss, 0],
                        [ss, ss, 0],
                        [-ss, ss, 0]])
        Kmat = np.array([[700, 0, 0],
                         [0, 700, 0],
                         [0, 0, 1]]) * 1.0
        disCoeffs = np.zeros([4, 1]) * 1.0
        ipoints = np.array([[-1, -1],
                            [1, -1],
                            [1, 1],
                            [-1, 1]])
        for point in ipoints:
            x = point[0]
            y = point[1]
            z = H[2, 0] * x + H[2, 1] * y + H[2, 2]
            point[0] = (H[0, 0] * x + H[0, 1] * y + H[0, 2]) / z * 1.0
            point[1] = (H[1, 0] * x + H[1, 1] * y + H[1, 2]) / z * 1.0
        campoint = ipoints * 1.0
        opoints = np.array([[-1.0, -1.0, 0.0],
                            [1.0, -1.0, 0.0],
                            [1.0, 1.0, 0.0],
                            [-1.0, 1.0, 0.0]])
        opoints = opoints * 0.5
        rate, rvec, tvec = cv2.solvePnP(opoints, campoint, Kmat, disCoeffs)
        point, jac = cv2.projectPoints(src, np.zeros(rvec.shape), tvec, Kmat, disCoeffs)
        points = np.int32(np.reshape(point, [4, 2]))
        distance = np.abs(t / np.linalg.norm(points[0] - points[1]))
        return distance


flag_me = 1  #1为蓝方，0为黄方
RWHEEL = 2
LWHEEL = 1
LFOOT = 4
RFOOT = 3
LSHOULDER = 7
LELBOW = 8
LHAND = 5
RSHOULDER = 6
RELBOW = 10
RHAND = 9

DISTANCE_FRONT = 3
DISTANCE_UP = 8
DISTANCE_RIGHT = 8
DISTANCE_LEFT = 7
TURN_SPEED = 350
pid = pid()
up = uptech.UpTech()


def init():
    up.CDS_SetAngle(LFOOT, 520, 384)
    up.CDS_SetAngle(RFOOT, 520, 384)
    up.CDS_SetAngle(LHAND, 980, 384)
    up.CDS_SetAngle(RHAND, 1023, 384)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 400, 384)
    up.CDS_SetAngle(RELBOW, 511, 384)
    time.sleep(0.5)
    up.CDS_SetAngle(LSHOULDER, 512, 384)
    up.CDS_SetAngle(RSHOULDER, 530, 384)  #调小往前，调大往后


def go():
    up.CDS_SetSpeed(RWHEEL, -300)
    up.CDS_SetSpeed(LWHEEL, 300)


def slow():
    up.CDS_SetSpeed(RWHEEL, -200)
    up.CDS_SetSpeed(LWHEEL, 200)


def boost():
    up.CDS_SetSpeed(RWHEEL, -480)
    up.CDS_SetSpeed(LWHEEL, 480)
    time.sleep(0.3)


def boost_back():
    up.CDS_SetSpeed(RWHEEL, 620)
    up.CDS_SetSpeed(LWHEEL, -620)
    time.sleep(0.3)


def back():
    up.CDS_SetSpeed(RWHEEL, 290)
    up.CDS_SetSpeed(LWHEEL, -290)


def left():
    up.CDS_SetSpeed(RWHEEL, -TURN_SPEED)
    up.CDS_SetSpeed(LWHEEL, -TURN_SPEED + 20)


def right():
    up.CDS_SetSpeed(RWHEEL, TURN_SPEED)
    up.CDS_SetSpeed(LWHEEL, TURN_SPEED + 20)


def slow_right():
    up.CDS_SetSpeed(RWHEEL, 250)
    up.CDS_SetSpeed(LWHEEL, 270)


def slow_left():
    up.CDS_SetSpeed(RWHEEL, -250)
    up.CDS_SetSpeed(LWHEEL, -230)


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


def push_tag_pre():
    up.CDS_SetAngle(LELBOW, 420, 700)
    up.CDS_SetAngle(RELBOW, 500, 700)
    up.CDS_SetAngle(LHAND, 650, 700)
    up.CDS_SetAngle(RHAND, 750, 700)
    time.sleep(0.2)
    up.CDS_SetAngle(LSHOULDER, 640, 700)
    up.CDS_SetAngle(RSHOULDER, 390, 700)
    up.CDS_SetAngle(LHAND, 550, 700)
    up.CDS_SetAngle(RHAND, 600, 700)
    time.sleep(0.3)
    up.CDS_SetAngle(LELBOW, 320, 700)
    up.CDS_SetAngle(RELBOW, 580, 700)


#推方块
def push_tag():  #550 600
    stop()
    up.CDS_SetAngle(LFOOT, 540, 500)
    up.CDS_SetAngle(RFOOT, 540, 500)
    up.CDS_SetAngle(LELBOW, 390, 700)
    up.CDS_SetAngle(RELBOW, 500, 700)
    up.CDS_SetAngle(LHAND, 650, 700)
    up.CDS_SetAngle(RHAND, 750, 700)
    time.sleep(0.2)
    up.CDS_SetAngle(LSHOULDER, 680, 600)
    up.CDS_SetAngle(RSHOULDER, 380, 600)
    up.CDS_SetAngle(LHAND, 550, 700)
    up.CDS_SetAngle(RHAND, 600, 700)
    time.sleep(0.3)
    up.CDS_SetAngle(LELBOW, 290, 700)
    up.CDS_SetAngle(RELBOW, 580, 700)
    time.sleep(0.4)
    up.CDS_SetAngle(LSHOULDER, 850, 1000)
    up.CDS_SetAngle(RSHOULDER, 180, 1000)
    time.sleep(0.3)
    up.CDS_SetAngle(LELBOW, 420, 900)
    up.CDS_SetAngle(RELBOW, 450, 900)
    time.sleep(0.5)
    # 恢复姿态
    recover()
    print('推方块')
    time.sleep(1)
    back()
    time.sleep(1.4)
    left()
    time.sleep(0.4)  #炸弹块在中/间
    # time.sleep(0.3) #炸弹块在两侧
    slow()
    time.sleep(0.5)


#复位
def recover():
    up.CDS_SetAngle(LFOOT, 540, 500)  # 大于前倾
    up.CDS_SetAngle(RFOOT, 540, 500)
    up.CDS_SetAngle(LELBOW, 370, 500)
    up.CDS_SetAngle(RELBOW, 511, 500)
    up.CDS_SetAngle(LHAND, 980, 500)
    up.CDS_SetAngle(RHAND, 1023, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(LSHOULDER, 512, 500)
    up.CDS_SetAngle(RSHOULDER, 530, 500)


#攻击1
def attack_1():
    #准备
    up.CDS_SetAngle(LSHOULDER, 850, 600)
    up.CDS_SetAngle(RSHOULDER, 300, 600)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 100, 600)
    up.CDS_SetAngle(RELBOW, 800, 600)
    up.CDS_SetAngle(LHAND, 550, 600)
    up.CDS_SetAngle(RHAND, 620, 600)
    time.sleep(0.5)
    #攻击
    up.CDS_SetAngle(LELBOW, 500, 900)
    up.CDS_SetAngle(RELBOW, 400, 900)
    time.sleep(0.5)
    #恢复
    up.CDS_SetAngle(LHAND, 980, 600)
    up.CDS_SetAngle(RHAND, 1023, 600)
    up.CDS_SetAngle(LELBOW, 400, 600)
    up.CDS_SetAngle(RELBOW, 490, 600)
    time.sleep(0.2)
    up.CDS_SetAngle(LSHOULDER, 512, 600)
    up.CDS_SetAngle(RSHOULDER, 530, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(RELBOW, 511, 700)
    up.CDS_SetAngle(LFOOT, 540, 500)
    up.CDS_SetAngle(RFOOT, 540, 500)


#前方攻击
def attack_F():
    # stop()
    up.CDS_SetAngle(LFOOT, 540, 800)
    up.CDS_SetAngle(RFOOT, 540, 800)
    up.CDS_SetAngle(LHAND, 880, 900)
    up.CDS_SetAngle(RHAND, 930, 900)
    up.CDS_SetAngle(LSHOULDER, 690, 900)
    up.CDS_SetAngle(RSHOULDER, 350, 900)
    time.sleep(0.2)
    up.CDS_SetAngle(LELBOW, 250, 900)
    up.CDS_SetAngle(RELBOW, 620, 900)
    time.sleep(0.3)
    up.CDS_SetAngle(LSHOULDER, 850, 1000)  #790 250
    up.CDS_SetAngle(RSHOULDER, 180, 1000)
    time.sleep(0.4)
    recover()

#左手攻击
def attack_L():
    #准备
    up.CDS_SetAngle(LSHOULDER, 850, 800)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 70, 800)
    up.CDS_SetAngle(LHAND, 580, 800)
    time.sleep(0.5)
    #攻击
    up.CDS_SetAngle(LELBOW, 470, 1000)
    time.sleep(0.5)
    #恢复
    up.CDS_SetAngle(LHAND, 980, 800)
    up.CDS_SetAngle(LELBOW, 400, 800)
    time.sleep(0.1)
    up.CDS_SetAngle(LSHOULDER, 512, 800)
    up.CDS_SetAngle(LFOOT, 540, 500)
    up.CDS_SetAngle(RFOOT, 540, 500)


#右手攻击
def attack_R():
    #准备
    up.CDS_SetAngle(RSHOULDER, 180, 800)
    time.sleep(0.5)
    up.CDS_SetAngle(RELBOW, 800, 800)
    up.CDS_SetAngle(RHAND, 620, 800)
    time.sleep(0.5)
    # # #攻击
    up.CDS_SetAngle(RELBOW, 400, 1000)
    time.sleep(0.5)
    #恢复
    up.CDS_SetAngle(RHAND, 1023, 800)
    up.CDS_SetAngle(RELBOW, 511, 800)
    time.sleep(0.1)
    up.CDS_SetAngle(RSHOULDER, 530, 800)
    up.CDS_SetAngle(LFOOT, 540, 500)
    up.CDS_SetAngle(RFOOT, 540, 500)


#后倾前起
def front_stand():
    up.CDS_SetAngle(RHAND, 500, 500)
    up.CDS_SetAngle(LHAND, 500, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LELBOW, 800, 500)
    up.CDS_SetAngle(RELBOW, 100, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LSHOULDER, 200, 500)
    up.CDS_SetAngle(RSHOULDER, 800, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(RHAND, 300, 500)
    up.CDS_SetAngle(LHAND, 250, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LFOOT, 420, 500)  # 大于前倾
    up.CDS_SetAngle(RFOOT, 420, 500)
    up.CDS_SetAngle(LELBOW, 400, 500)
    up.CDS_SetAngle(RELBOW, 511, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LSHOULDER, 280, 384)
    up.CDS_SetAngle(RSHOULDER, 750, 384)
    time.sleep(0.4)
    up.CDS_SetAngle(RHAND, 500, 500)
    up.CDS_SetAngle(LHAND, 600, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LSHOULDER, 350, 500)
    up.CDS_SetAngle(RSHOULDER, 650, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LFOOT, 500, 400)  # 大于前倾
    up.CDS_SetAngle(RFOOT, 500, 400)
    up.CDS_SetAngle(LELBOW, 450, 500)
    up.CDS_SetAngle(RELBOW, 470, 500)
    time.sleep(0.4)
    #恢复
    up.CDS_SetAngle(LHAND, 980, 500)
    up.CDS_SetAngle(RHAND, 1023, 500)
    up.CDS_SetAngle(LFOOT, 520, 500)
    up.CDS_SetAngle(RFOOT, 520, 500)
    time.sleep(0.4)
    up.CDS_SetAngle(LSHOULDER, 512, 500)
    up.CDS_SetAngle(RSHOULDER, 530, 500)
    time.sleep(0.2)
    up.CDS_SetAngle(LELBOW, 370, 500)
    up.CDS_SetAngle(RELBOW, 511, 500)
    up.CDS_SetAngle(LFOOT, 540, 500)
    up.CDS_SetAngle(RFOOT, 540, 500)


#前倾后起
def back_stand():
    up.CDS_SetAngle(RHAND, 500, 500)
    up.CDS_SetAngle(LHAND, 500, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(LELBOW, 800, 500)
    up.CDS_SetAngle(RELBOW, 100, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(RSHOULDER, 200, 500)
    up.CDS_SetAngle(LSHOULDER, 850, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(RHAND, 900, 500)
    up.CDS_SetAngle(LHAND, 850, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(LFOOT, 720, 500)  # 大于前倾
    up.CDS_SetAngle(RFOOT, 720, 500)
    up.CDS_SetAngle(LELBOW, 400, 500)
    up.CDS_SetAngle(RELBOW, 511, 500)
    time.sleep(0.5)
    up.CDS_SetAngle(LSHOULDER, 650, 256)
    up.CDS_SetAngle(RSHOULDER, 350, 256)
    time.sleep(0.5)
    up.CDS_SetAngle(RHAND, 650, 256)
    up.CDS_SetAngle(LHAND, 650, 256)
    time.sleep(0.5)
    #恢复
    up.CDS_SetAngle(LFOOT, 560, 300)
    up.CDS_SetAngle(RFOOT, 560, 300)
    up.CDS_SetAngle(LSHOULDER, 512, 400)
    up.CDS_SetAngle(RSHOULDER, 530, 400)
    up.CDS_SetAngle(LELBOW, 370, 400)
    up.CDS_SetAngle(RELBOW, 511, 400)
    up.CDS_SetAngle(LFOOT, 540, 400)
    up.CDS_SetAngle(RFOOT, 540, 400)
    up.CDS_SetAngle(LHAND, 980, 400)
    up.CDS_SetAngle(RHAND, 1023, 400)


#登台
def up_platform():
    # 上坡
    # up.CDS_SetAngle(LFOOT, 600, 500)  # 大于前倾
    # up.CDS_SetAngle(RFOOT, 600, 500)
    up.CDS_SetSpeed(RWHEEL, -300)
    up.CDS_SetSpeed(LWHEEL, 300)
    # time.sleep(2.2) #炸弹块在右侧
    # time.sleep(1.6) #炸弹块在中间或左侧
    time.sleep(1)
    # 进入擂台
    # up.CDS_SetAngle(LFOOT, 540, 384)  # 大于前倾
    # up.CDS_SetAngle(RFOOT, 540, 384)
    up.CDS_SetSpeed(RWHEEL, -400)
    up.CDS_SetSpeed(LWHEEL, 650)
    # time.sleep(1.1) #炸弹块在右侧
    time.sleep(1.5)  #炸弹块在中间或左侧


#停止行动信号
def signal_handler(signal, frame):
    stop()
    exit(0)


#边缘检测
def edge_detect():
    #1为没检测到，0为检测到
    if zuo_qian_hw == 1 and you_qian_hw == 1:
        slow()
        time.sleep(0.15)
        back()
        time.sleep(0.6)
        right()
        time.sleep(0.4)
    elif zuo_qian_hw == 1 and you_qian_hw == 0:
        slow()
        time.sleep(0.15)
        back()
        time.sleep(0.6)
        right()
        time.sleep(0.4)
    elif zuo_qian_hw == 0 and you_qian_hw == 1:
        slow()
        time.sleep(0.15)
        back()
        time.sleep(0.6)
        left()
        time.sleep(0.4)


# 方块检测及推动
def tag_detect():
    global flag_push
    global flag_push_pre
    distance = 0
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    results = atag.detect(gray)  # 对灰度图进行检测，结果放results列表里
    results_len = len(results)  # 看results里有没有识别到
    index = 0
    go()
    if results:
        tag0 = 0
        tag1 = 0
        if results_len > 1:
            for i in range(1, results_len):
                if atag.get_distance(results[index].homography, 4300) > atag.get_distance(results[i].homography, 4300):
                    index = i
        distance = int(atag.get_distance(results[index].homography, 4300))
        print('距离：',distance)
        print('ID:',results[index].tag_id)

        tag_id = results[index].tag_id
        if tag_id == 1 and flag_me == 0:
            tag1 = 1
            tag_x = np.array(results[index].center).astype(int)[1]
            input_value = tag_x - 211
            pid_output = pid.update(input_value, 0)
            # print(f"x:{tag_x},pidout:{pid_output}")
            if distance < 125:
                up.CDS_SetSpeed(RWHEEL, -330 + 10 - pid_output)
                up.CDS_SetSpeed(LWHEEL, 330 - pid_output)
            else:
                edge_detect()
            # mid1 = tuple(results[index].corners[0].astype(int))[0] / 2 + tuple(results[index].corners[2].astype(int))[
            #     0] / 2
            # print(mid1)
        elif tag_id == 0 and flag_me == 1:
            tag0 = 1
            tag_x = np.array(results[index].center).astype(int)[1]
            input_value = tag_x - 211
            pid_output = pid.update(input_value, 0)
            # print(f"x:{tag_x},pidout:{pid_output}")
            if distance < 125:
                up.CDS_SetSpeed(RWHEEL, -330 + 10 - pid_output)
                up.CDS_SetSpeed(LWHEEL, 330 - pid_output)
            else:
                edge_detect()
            # mid0 = tuple(results[index].corners[0].astype(int))[0] / 2 + tuple(results[index].corners[2].astype(int))[
            #     0] / 2
            # print("mid0为:",mid0)
    else:
        tag0 = 0
        tag1 = 0
    #

    if flag_me == 1:
        if tag0 == 1:
            # if flag_push_pre==1:
            #     push_tag_pre()
            #     flag_push_pre=0
            if flag_push == 1 and (qian_hw == 0 or zheng_zuo_qian_hw == 0 or zheng_you_qian_hw == 0) and distance < 45:
                # slow()
                # time.sleep(0.2)
                push_tag()
                flag_push = 0
                print('hhh')
        else:
            edge_detect()
            flag_push = 1
            # flag_push_pre=1
    #
    elif flag_me == 0:
        if tag1 == 1:
            # if flag_push_pre==1:
            #     push_tag_pre()
            #     flag_push_pre=0
            if flag_push == 1 and (qian_hw == 0 or zheng_zuo_qian_hw == 0 or zheng_you_qian_hw == 0) and distance < 45:
                # slow()
                # time.sleep(0.2)
                push_tag()
                flag_push = 0
                print('hhh')
                # stop()
        else:
            edge_detect()
            flag_push = 1
            # flag_push_pre = 1

#倒地起身
def stand():
    global ANGLE_qian
    global ANGLE_hou
    global flag_stand

    flag_stand = 1
    if ANGLE_qian == 0 and ANGLE_hou == 1:
        flag_stand = 0
    if flag_stand == 0:
        stop()
        front_stand()
        flag_stand=1
        # if qian_hw == 1:
        #     back_stand()
        #     flag_stand = 1
        # if qian_hw == 0:
        #     back_stand()
        #     flag_stand = 1


#敌人检测及攻击
def enemy_detect():
    # if 550>adc_data[DISTANCE_FRONT] > 380:
    #     stop()
    #     attack_F()
    #     time.sleep(1)
    if 920>adc_data[DISTANCE_LEFT] > 550:
        stop()
        attack_L()
        time.sleep(1)
    # elif 920>adc_data[DISTANCE_RIGHT] > 550:
    #     stop()
    #     attack_R()
    #     time.sleep(1)
    # if qian_hw==0:
    #     stop()
    #     attack_F()
    #     time.sleep(1)
    # if zheng_zuo_qian_hw==0:
    #     stop()
    #     attack_L()
    #     time.sleep(1)
    # elif zheng_you_qian_hw==0:
    #     stop()
    #     attack_R()
    #     time.sleep(1)

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)  #停止行动信号
    io_data = []
    up.ADC_IO_Open()
    up.CDS_Open()
    adc_data = []
    atag = Atag()
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    up.CDS_SetMode(LWHEEL, 1)
    up.CDS_SetMode(RWHEEL, 1)
    up.CDS_SetMode(LFOOT, 0)
    up.CDS_SetMode(RFOOT, 0)
    up.CDS_SetMode(LSHOULDER, 0)
    up.CDS_SetMode(RSHOULDER, 0)
    up.CDS_SetMode(LELBOW, 0)
    up.CDS_SetMode(RELBOW, 0)
    up.CDS_SetMode(LHAND, 0)
    up.CDS_SetMode(RHAND, 0)
    time.sleep(0.05)
    #无接触启动
    recover()
    # up.CDS_SetAngle(LELBOW,370,500)
    print('ok')
    while True:
        adc_data = up.ADC_Get_All_Channle()
        # print(adc_data[DISTANCE_UP])
        if adc_data[DISTANCE_UP] > 920:
            break

    # up.CDS_SetSpeed(RWHEEL, -350)
    # up.CDS_SetSpeed(LWHEEL, 350)
    # time.sleep(0.5)
    # up.CDS_SetSpeed(RWHEEL, -400)
    # up.CDS_SetSpeed(LWHEEL, 650)
    # time.sleep(0.5)
    # up_platform()
    # attack_L()
    # up.CDS_SetAngle(LELBOW, 700, 500)
    # print('ok')
    # push_tag()
    # 429手臂最长距离
    flag_push = 1
    # flag_push_pre=1
    while True:
        adc_data = up.ADC_Get_All_Channle()
        #io读取
        io_all_input = up.ADC_IO_GetAllInputLevel()
        io_array = '{:08b}'.format(io_all_input)
        io_arr = io_array.replace('-', '')
        io_data = []
        for index, value in enumerate(io_arr):
            io = int(value)
            io_data.insert(0, io)
        zuo_qian_hw = io_data[3]
        you_qian_hw = io_data[1]
        ANGLE_qian = io_data[0]  #1为水平 0为倾斜
        ANGLE_hou = io_data[7]  #0为水平 1为倾斜
        qian_hw = io_data[6]
        zheng_zuo_qian_hw = io_data[5]
        zheng_you_qian_hw = io_data[7]

        # go()
        # stand()
        front_stand()
        # edge_detect()
        # print(ANGLE_hou)
        # tag_detect()
        # enemy_detect()
