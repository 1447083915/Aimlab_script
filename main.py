import pyautogui
import numpy as np
from BotRecognition import circle_bot_recognition, color_match
import time
import win32api
import win32con
# from PIL import Image, ImageDraw


# 获取曼哈顿距离最小的目标
def get_min_manhattan_dis_center(centers):
    # 获取当前鼠标坐标
    center_x, center_y = win32api.GetCursorPos()
    move_x, move_y = 0, 0
    final_x, final_y = center_x, center_y
    min_mht_dis = 3000
    for target_x, target_y in centers:
        tmp_mht_dis = abs(target_x - center_x) + abs(target_y - center_y)
        if tmp_mht_dis < min_mht_dis:
            min_mht_dis = tmp_mht_dis
            final_x, final_y = target_x, target_y
            move_x, move_y = (target_x - center_x), (target_y - center_y)
    return move_x, move_y, final_x, final_y


time.sleep(5)
# 获取初始信息
sensitivity = 0.14
target_color = (200, 60, 200)  # 目标颜色均值
screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)
center_x, center_y = screen_width // 2, screen_height // 2

# 鼠标左键开火
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
time.sleep(0.1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
time.sleep(1)

start = time.time()
end = time.time()
# 二次瞄准策略
while end - start < 59:
    # 截取屏幕
    screenshot = pyautogui.screenshot()
    # 转换为numpy数组
    screenshot = np.array(screenshot)
    # 获取球体中心
    circle_centers = circle_bot_recognition(screenshot, target_color)
    move_x, move_y, final_x, final_y = get_min_manhattan_dis_center(circle_centers)

    # 移动鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,
                         int((move_x/0.1325)*0.9),
                         int((move_y/0.1325)*0.9), 0, 0)
    time.sleep(0.01)
    # 截取屏幕
    screenshot = pyautogui.screenshot()
    # 转换为numpy数组
    screenshot = np.array(screenshot)
    # 获取球体中心
    circle_centers = circle_bot_recognition(screenshot, target_color)
    move_x, move_y, final_x, final_y = get_min_manhattan_dis_center(circle_centers)

    # 移动鼠标
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,
                         int((move_x / 0.1325)),
                         int((move_y / 0.1325)), 0, 0)
    time.sleep(0.01)
    # 鼠标左键开火
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    end = time.time()
# while end - start < 10:
#     # 截取屏幕
#     screenshot = pyautogui.screenshot()
#     # 转换为numpy数组
#     screenshot = np.array(screenshot)
#     # 获取球体中心
#     circle_centers = circle_bot_recognition(screenshot, target_color)
#     move_x, move_y, final_x, final_y = get_min_manhattan_dis_center(circle_centers)
#
#     # # 将final_x, final_y的像素位置标记在截图上
#     # marked_image = Image.fromarray(screenshot)
#     # draw = ImageDraw.Draw(marked_image)
#     # draw.ellipse([(center_x + move_x - 2, center_y + move_y - 2),
#     #                 (center_x + move_x + 2, center_y + move_y + 2)],
#     #                 fill='blue', outline='blue')
#     # draw.rectangle([final_x - 5, final_y - 5, final_x + 5, final_y + 5], outline='red',
#     #                width=2)  # 在final_x, final_y处画一个红色的矩形
#     # del draw
#     #
#     # # 保存标记后的截图
#     # marked_image.save(f'TestImage/Trace/marked_screenshot_{i}.png')
#
#     # 移动鼠标
#     win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,
#                          int(move_x/0.1325),
#                          int(move_y/0.1325), 0, 0)
#     time.sleep(0.1)
#     # 鼠标左键开火
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
#     time.sleep(0.05)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
#     end = time.time()
