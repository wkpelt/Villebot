import pyautogui, sys
import time
import pyperclip
import random

print('Press Ctrl-C to quit.')

correctAnswers = []
rightAnswer = []
texts = []
locations = []

while True:
    print("Montako kysymystä?")
    questions = int(input())
    break
while (len(correctAnswers)) < questions:
    pyautogui.scroll(-2000)
    time.sleep(1)
    pos = None
    while pos is None:
        for pos in pyautogui.locateAllOnScreen('blue.png'):
            pyautogui.moveTo(pos[0]+5,pos[1]+5)
            pyautogui.dragRel(650, 40, 0.5, button='left')
            pyautogui.hotkey('ctrl', 'c')
            texts.append(   pyperclip.paste()  ,  (pos[0],pos[1])   )
            locations.append(pos[0],post[1])
            # print (pos)
            # print (locations)
        choices = len(texts)
        print("Valintoja yhteensä:", choices)
        for i in texts:
            if i in correctAnswers:
                pyautogui.click(i[1])
        texts = []

    while True:
        if pyautogui.locateCenterOnScreen('green.png') == None:
            x,y = locations[0][0],locations[0][1]
            pyautogui.click(x,y)

        if pyautogui.locateCenterOnScreen('green.png') != None:
            print("correct answer")
            green = pyautogui.locateOnScreen('green.png')
            pyautogui.moveTo(green[0],green[1])
            pyautogui.dragRel(700, 50, 0.5, button='left')
            pyautogui.hotkey('ctrl', 'c')
            if pyperclip.paste() in correctAnswers:
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
            else:
                correctAnswers.append(pyperclip.paste())
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
            break

        else:
            print("wrong answer")
            pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
