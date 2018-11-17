import pyautogui
import time
import pyperclip
import random
import string

print('Press Ctrl-Alt-Del to stop the bot.')

texts = []
locations = []
choices = []
last = []
wrong = []
correctAnswers = []
task = 0

print("Montako kysymystä?")
questions = int(input())

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
                copiedText = pyperclip.paste()
                copiedText.splitlines()
                texts.append(copiedText)
                last.append(copiedText)
                locations.append((pos[0]+5,pos[1]+5))
                choices.append((pos[0]+5,pos[1]+5))
                if len(correctAnswers) > task:
                    for i in range(len(texts)):
                        if (texts[i] in correctAnswers[task]):
                            pyautogui.click(locations[i])
                            done = True

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
            print("\nCorrect answer:")
            print(last[-1],"\n")
            task += 1
            if last[-1] in correctAnswers:
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                time.sleep(0.2)
                pyautogui.click(pyautogui.locateCenterOnScreen('next2.png'))
                break
            else:
                wrong = []
                green = pyautogui.locateOnScreen('green.png')
                pyautogui.moveTo(green[0],green[1])
                pyautogui.dragRel(700, 45, 0.2, button='left')
                pyautogui.hotkey('ctrl', 'c')
                correctAnswer = pyperclip.paste()
                correctAnswer.splitlines()
                if len(correctAnswer) > 1:
                    correctAnswer = correctAnswer[1]
                correctAnswers.append(correctAnswer)
                pyautogui.click(pyautogui.locateCenterOnScreen('next.png'))
                time.sleep(0.2)
                pyautogui.click(pyautogui.locateCenterOnScreen('next2.png'))
                break

        if pyautogui.locateOnScreen('green.png') == None:
            task = 0
            print("\nWrong answer:")
            print(n,"\n")
            wrong.append(n)
            pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
            for i in range(5):
                pyautogui.press('pgdn')
            break

print("Correct answers: ")
nr = 1
for i in correctAnswers
    print(nr,": ",i)
    nr += 1
while True:
    pass
