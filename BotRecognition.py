import numpy as np
import cv2


def color_match(color1, color2, tolerance=50):
    # 检查两个颜色是否接近，根据给定的容差值
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))


# 识别对应颜色的球体目标
def circle_bot_recognition(image, target_color):
    # 转换为 HSV 色彩空间
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 定义阈值以提取鲜艳的颜色 (可以调整这些值以适应不同的图像)
    lower_vibrant = np.array([25, 100, 100])  # 下限的HSV值
    upper_vibrant = np.array([255, 255, 255])  # 上限的HSV值

    # 创建掩码以提取鲜艳的颜色
    mask = cv2.inRange(hsv_image, lower_vibrant, upper_vibrant)

    # 球体识别
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT,
                               dp=1, minDist=50,
                               param1=14, param2=10,
                               minRadius=2, maxRadius=100)
    circles = circles[0, :]
    circle_centers = []
    # 确保至少检测到一个圆
    if circles is not None:
        for (x, y, r) in circles:
            # 检查圆心的颜色是否与目标颜色相匹配
            if color_match(image[int(y), int(x)], target_color):
                circle_centers.append((x, y))
    return circle_centers


if __name__ == "__main__":
    target_color = (200, 60, 200)  # 目标颜色均值
    # 读取图片
    image = cv2.imread('TestImage/SixShot/Bot_1.jpg')
    image = np.array(image)
    circle_centers = circle_bot_recognition(image, target_color)
    for (x, y) in circle_centers:
        cv2.circle(image, (int(x), int(y)), 4, (0, 0, 255), 2)

    cv2.imshow("Detected Circles", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
