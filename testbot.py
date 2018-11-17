import pyautogui, sys
import time
import pyperclip
import random
import string

print('Press Ctrl-Alt-Del to stop the bot.')

correctAnswers = []
texts = []
locations = []
choices = []
last = ['none','none','none','none','none']
wrong = []
tehtävä = 0

while True:
    print("Montako kysymystä?")
    questions = int(input())
    break
while (len(correctAnswers)) < questions-1:
    time.sleep(1)
    for i in range(5):
        pyautogui.press('pgdn')
    pos = None
    done = False
    while pos is None:
        for pos in pyautogui.locateAllOnScreen('blue2.png'):
            if done == False:
                pyautogui.moveTo(pos[0]-20,pos[1]+5)
                pyautogui.dragRel(700, 45, 0.2, button='left')
                pyautogui.hotkey('ctrl', 'c')
                valinta = pyperclip.paste()
                valinta.splitlines()
                texts.append(valinta)
                last.append(valinta)
                locations.append((pos[0]+5,pos[1]+5))
                choices.append((pos[0]+5,pos[1]+5))
                if len(correctAnswers) > tehtävä:
                    for i in range(len(texts)):
                        print(len(correctAnswers))
                        print(tehtävä)
                        if (texts[i] in correctAnswers[tehtävä]):
                            pyautogui.click(locations[i])
                            done = True

        print("Correct answers: ",correctAnswers)
        print("Choices : ",texts)
        print("Wrong answers: ",wrong)
        texts = []
        locations = []

    while True:
        if last[-1] in wrong:
            pass
            if last[-2] in wrong:
                pass
                if last[-3] in wrong:
                    pass
                    if last[-4] in wrong:
                        pyautogui.click(choices[-5])
                        n = last[-5]
                    else:
                        pyautogui.click(choices[-4])
                        n = last[-4]
                else:
                    pyautogui.click(choices[-3])
                    n = last[-3]
            else:
                pyautogui.click(choices[-2])
                n = last[-2]
        else:
            pyautogui.click(choices[-1])
            n = last[-1]

        if pyautogui.locateOnScreen('green.png') != None:
            print("Correct answer\n")
            tehtävä += 1
            if last[-1] in correctAnswers:
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                time.sleep(0.5)
                pyautogui.click(pyautogui.locateCenterOnScreen('next2.png'))
                break
            else:
                wrong = []
                green = pyautogui.locateOnScreen('green.png')
                pyautogui.moveTo(green[0],green[1])
                pyautogui.dragRel(700, 45, 0.2, button='left')
                pyautogui.hotkey('ctrl', 'c')
                rightAnswer = pyperclip.paste()
                rightAnswer = rightAnswer.splitlines()
                if len(rightAnswer) > 1:
                    rightAnswer = rightAnswer[1]
                correctAnswers.append(rightAnswer)
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                time.sleep(0.5)
                pyautogui.click(pyautogui.locateCenterOnScreen('next2.png'))
                break

        if pyautogui.locateOnScreen('green.png') == None:
            tehtävä = 0
            print("Wrong answer\n")
            wrong.append(n)
            pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
            for i in range(5):
                pyautogui.press('pgdn')
            break
