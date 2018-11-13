import pyautogui
pos = None
while True:
    while pos is None:
        for pos in pyautogui.locateAllOnScreen('blue.png'):
            print(pos)
