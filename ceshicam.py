#!/usr/bin/env python3
# coding: UTF-8
import apriltag
import cv2
import numpy as np
distance = 0
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

if __name__ == '__main__':
    atag = Atag()  # 实例化atag
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    x = 2
    y = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)# 转换为灰度图像
        cv2.imshow("frame", gray)
        cv2.waitKey(1)
        results = atag.detect(gray)  # 对灰度图进行检测，结果放results列表里
        results_len = len(results)  # 看results里有没有识别到
        if results:
            tag0 = 0
            tag1 = 0
            tag2 = 0
            for result in results:
                # print("Detected tag ID:", result.tag_id)
                distance = atag.get_distance(result.homography, 4300)
                print(f'distance:{distance}')
                y = distance
                if (result.tag_id == 1):
                    tag1 = 1
                    mid1 = tuple(result.corners[0].astype(int))[0] / 2 + tuple(result.corners[2].astype(int))[0] / 2
                    # print("mid1为:",mid1)
                    # print()
                elif (result.tag_id == 0):
                    tag0 = 1
                    mid0 = tuple(result.corners[0].astype(int))[0] / 2 + tuple(result.corners[2].astype(int))[0] / 2
                    # print("mid0为:",mid0)
                    print(tuple(result.corners[1].astype(int))[0])
                elif (result.tag_id == 2):
                    tag2 = 1
                    mid2 = tuple(result.corners[0].astype(int))[0] / 2 + tuple(result.corners[2].astype(int))[0] / 2
                # print("mid0为",mid0,"mid1为",mid1,"mid2为",mid2)
                tag_thing = 0
        else:
            tag0 = 0
            tag1 = 0
            tag2 = 0
            tag_thing = 1
            # print("tag_thing为",tag_thing)

