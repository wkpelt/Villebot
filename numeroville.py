import pyautogui
import time
import pyperclip

#määritä x
x = 0
incorrect = "Incorrect!"
time.sleep(4)
#määritä restart
restart = pyautogui.locateCenterOnScreen('restart.png')

while True:
    pyautogui.click(restart)
    
    #määritä monesko tehtävä
    #pyautogui.press('enter')
    #pyautogui.press('enter')
    
    pyautogui.press('tab')
    pyautogui.press('tab')
    num = str(x)
    pyautogui.typewrite(num)
    x += 1
    pyautogui.press('enter')
    time.sleep(0.1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    text = pyperclip.paste()
    if incorrect in text:
        print(text)
    else:
        break
