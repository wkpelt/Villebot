import pyautogui,sys
import time
import pyperclip
import string
import PySimpleGUI as sg

print('Press Ctrl-Alt-Del to stop the bot.')

texts = []
locations = []
choices = []
last = ['none','none','none','none','none']
wrong = []
correctAnswers = []
task = 0

layout = [[sg.Text('Montako kysymystä?'), sg.Text('', key='_OUTPUT_') ],
          [sg.Input(do_not_clear=False, key='_IN_')],
          [sg.Multiline('', key='_STUFF_',do_not_clear=True,size=(35, 3))],
          [sg.Output(size=(80,10))],
          [sg.Button('OK'),sg.Button('Start'),sg.Button('Pause'),sg.Button('Unpause'),sg.Exit()]]
window = sg.Window('VILLEbot v0.9', keep_on_top = True).Layout(layout)
#pyautogui.press('f11')

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    if event == 'OK':
        questions = int(values['_IN_'])
        window.FindElement('_OUTPUT_').Update(values['_IN_'])
        #window.FindElement('_STUFF_').Update(values['_IN_'])
        #sg.Print(values['_IN_'],keep_on_top = True)
    if event == 'Start':
        while (len(correctAnswers)) < questions-1:
            print(event)
            time.sleep(0.2)
            for i in range(5):
                pyautogui.press('pgdn')
            time.sleep(1)
            pos = None
            done = False
            #window.FindElement('_STUFF_').Update("Task nr: ",task,"\nLength of correctAnswers: ",len(correctAnswers))
            print("Task nr: ",task)
            print("Length of correctAnswers: ",len(correctAnswers))
            window.Read()
            while pos is None:
                for pos in pyautogui.locateAllOnScreen('blue2.png'):
                    if done == False:
                        pyautogui.moveTo(pos[0]-20,pos[1]+5)
                        pyautogui.dragRel(700, 45, 0.2, button='left')
                        pyautogui.hotkey('ctrl', 'c')
                        copiedText = pyperclip.paste()
                        copiedText.strip("\r\n")
                        texts.append(copiedText)
                        last.append(copiedText)
                        locations.append((pos[0]+5,pos[1]+5))
                        choices.append((pos[0]+5,pos[1]+5))
                        window.Read()
                        if len(correctAnswers) > task:
                            for i in range(len(texts)):
                                if (texts[i] in correctAnswers[task]):
                                    pyautogui.click(locations[i])
                                    window.Read()
                                    done = True

                print("Correct answers: ",correctAnswers)
                print("Wrong answers: ",wrong)
                print("\nVäärien määrä: ",len(wrong))
                texts = []
                locations = []
                window.Read()

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

                window.Read()
                if pyautogui.locateOnScreen('green.png') != None:
                    print("\nCorrect answer:")
                    print(last[-1],"\n")

                    for i in range(5):
                        pyautogui.press('pgdn')
                    task += 1
                    if last[-1] in correctAnswers:
                        next2 = pyautogui.locateCenterOnScreen('next2.png')
                        next = pyautogui.locateCenterOnScreen('next.png')
                        if next is None:
                            pyautogui.click(next2)
                        else:
                            pyautogui.click(next)
                        for i in range(5):
                            pyautogui.press('pgdn')
                        time.sleep(0.5)
                        window.Read()
                        break
                    else:
                        wrong = []
                        green = pyautogui.locateOnScreen('green.png')
                        pyautogui.moveTo(green[0],green[1])
                        pyautogui.dragRel(700, 45, 0.2, button='left')
                        pyautogui.hotkey('ctrl', 'c')
                        rightAnswer = pyperclip.paste()
                        correctAnswers.append(rightAnswer.strip("\r\n"))
                        next2 = pyautogui.locateCenterOnScreen('next2.png')
                        next = pyautogui.locateCenterOnScreen('next.png')
                        if next is None:
                            pyautogui.click(next2)
                        else:
                            pyautogui.click(next)
                        for i in range(5):
                            pyautogui.press('pgdn')
                        time.sleep(0.5)
                        window.Read()
                        break

                if pyautogui.locateOnScreen('green.png') == None:
                    if len(wrong) > 5:
                        wrong = []
                    task = 0
                    print("\nWrong answer:")
                    print(n,"\n")
                    wrong.append(n)
                    pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
                    window.Read()
                    for i in range(5):
                        pyautogui.press('pgdn')
                    break

        print("Correct answers: ")
        nr = 1
        for i in correctAnswers:
            print(nr,": ",i)
            nr += 1
        while True:
            window.Read()
window.Close()
