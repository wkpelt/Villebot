import pyautogui, sys
import time
import pyperclip
import random

print('Press Ctrl-C to quit.')

pos = None
correctAnswers = []
rightAnswer = []
texts = []
locations = []

while True:
    print("Montako kysymystä?")
    questions = int(input())
    break
while (len(correctAnswers)) < questions:
    pyautogui.press('pgdn')
    time.sleep(1)
    while pos is None:
        for pos in pyautogui.locateAllOnScreen('blue.png'):
            pyautogui.moveTo(pos[0]+5,pos[1]+5)
            pyautogui.dragRel(650, 40, 0.5, button='left')
            pyautogui.hotkey('ctrl', 'c')
            k = pyperclip.paste()
            if k in correctAnswers:
                pyautogui.click(pos[0],pos[1])
            texts.append(k)
            locations.append(pos)
            print (pos)
            print (locations)
        choices = len(texts)
        print("Valintoja yhteensä:", choices)
        for i in texts:
            print(i)

    while True:
        if pyautogui.locateCenterOnScreen('green.png') == None:
            
            x,y = locations[0][0],locations[0][1]
            pyautogui.click(x,y)

        if pyautogui.locateCenterOnScreen('green.png') != None:
            print("correct answer")
            green = pyautogui.locateOnScreen('green.png')
            pos = None
            if k in correctAnswers:
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                break
            else:
                pyautogui.moveTo(green[0],green[1])
                pyautogui.dragRel(700, 50, 0.5, button='left')
                pyautogui.hotkey('ctrl', 'c')
                correctAnswers.append(pyperclip.paste())
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                break

        else:
            print("wrong answer")
            pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
