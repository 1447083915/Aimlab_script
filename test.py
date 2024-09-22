import time

import win32api
import win32con
import win32gui
import numpy as np
import win32ui
from PIL import Image

def capture_screen():
    # 获取整个屏幕的设备上下文
    hdesktop = win32gui.GetDesktopWindow()
    hwndDC = win32gui.GetWindowDC(hdesktop)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    # 获取屏幕的宽度和高度
    width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    print(width, height)

    # 创建一个位图对象
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
                                      win32api.GetSystemMetrics(win32con.SM_CYSCREEN))

    # 将截图保存到位图对象中
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (win32api.GetSystemMetrics(win32con.SM_CXSCREEN),
                           win32api.GetSystemMetrics(win32con.SM_CYSCREEN)), mfcDC, (0, 0), win32con.SRCCOPY)

    # 将位图对象转换为 PIL 图像
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    img = Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1)

    # 清理资源
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hdesktop, hwndDC)

    return img

# 示例：捕获屏幕并保存为文件
if __name__ == '__main__':
    screenshot = capture_screen()
    screenshot.save('screenshot.png')
