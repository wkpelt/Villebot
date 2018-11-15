import pyautogui, sys
import time
import pyperclip
import random
import string

print('Press Ctrl-C to quit.')

correctAnswers = []
texts = []
locations = []
last = []

while True:
    print("Montako kysymystä?")
    questions = int(input())
    break
while (len(correctAnswers)) < questions:
    pyautogui.scroll(-2000)
    time.sleep(1)
    pyautogui.scroll(-2000)
    pyautogui.scroll(-2000)
    pos = None
    done = False
    while pos is None:
        for pos in pyautogui.locateAllOnScreen('blue.png'):
            if done == False:
                pyautogui.scroll(-2000)
                pyautogui.moveTo(pos[0]-20,pos[1]+5)
                pyautogui.dragRel(700, 37, 0.2, button='left')
                pyautogui.hotkey('ctrl', 'c')
                valinta = pyperclip.paste()
                valinta = valinta.split(".")
                valinta = valinta[0]
                valinta.splitlines()
                texts.append(valinta)
                last.append(valinta)
                locations.append((pos[0],pos[1]))
                for i in range(len(texts)):
                    if (texts[i] in correctAnswers):
                        pyautogui.click(locations[i])
                        done = True
                        # pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                        # time.sleep(1)
                print(correctAnswers)
                print(texts)
        choices = len(texts)
        print("Valintoja yhteensä:", choices)
        amountCorrect = len(correctAnswers)
        texts = []
        locations = []

    while True:
        pyautogui.click(pyautogui.locateCenterOnScreen('blue.png'))
        time.sleep(1)
        if pyautogui.locateOnScreen('green.png') == None:
            print("wrong answer")
            pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
            break

        elif pyautogui.locateOnScreen('green.png') != None:
            print("correct answer")
            # for i in range(len(last)):
            #     if (last[i] not in correctAnswers):
            green = pyautogui.locateOnScreen('green.png')
            pyautogui.moveTo(green[0],green[1])
            pyautogui.dragRel(700, 50, 0.2, button='left')
            pyautogui.hotkey('ctrl', 'c')
            rightAnswer = pyperclip.paste()
            rightAnswer = rightAnswer.split(".")
            rightAnswer = rightAnswer[0]
            rightAnswer = rightAnswer.splitlines()
            if len(rightAnswer) > 1:
                rightAnswer = rightAnswer[1]
            if rightAnswer in correctAnswers:
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                pyautogui.click(pyautogui.locateCenterOnScreen('next2.png'))
                pyautogui.scroll(-2000)
                break
            else:
                correctAnswers.append(rightAnswer)
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                pyautogui.click(pyautogui.locateCenterOnScreen('next2.png'))
                pyautogui.scroll(-2000)
                break
