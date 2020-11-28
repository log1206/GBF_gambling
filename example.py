import pyautogui

#目前滑鼠坐標
pyautogui.position()
#目前螢幕解析度
pyautogui.size()
#(x,y)是否在螢幕上
x, y = 122, 244
pyautogui.onScreen(x, y)

#用num_seconds秒的时间把光标移动到(x, y)位置
num_seconds = 1.2
pyautogui.moveTo(x, y, duration=num_seconds)