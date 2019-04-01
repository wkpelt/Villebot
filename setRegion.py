import pyautogui
from pynput.mouse import Listener

x1, y1, x2, y2 = 0, 0, 0 ,0
clicked = 0

def on_click(x, y, button, pressed):
    global clicked, x1,y1,x2,y2
    if not pressed:
        print("Mouse clicked!")
        print(x,y)
        clicked += 1
        if (clicked == 1):
            x1 = x
            y1 = y
            print("x1y1 saved")
            print(x1,y1,x2,y2)
        elif (clicked == 2):
            x2 = x
            y2 = y
            print(x1,y1,x2,y2)
            image = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))
            image.save('testing.png')
            print("saved")
    else:
        pass

listener = Listener(on_click=on_click)
listener.start()
print(pyautogui.size())
