import pyautogui,sys
import os
import time
import pyperclip
import string
import PySimpleGUI as sg
from os import path

def main():

    print('Press Ctrl-Alt-Del to stop the bot.')
    texts = []
    locations = []
    choices = []
    last = ['none','none','none','none','none']
    correctAnswers = []
    wrong = []
    task = 0


    layout = [[sg.Text('Montako kysymystä?'), sg.Text('', key='_OUTPUT_', text_color=('blue')) ],
              [sg.Input(size=(40,3),do_not_clear=False, key='_IN_')],
              [sg.Text('Tehtäväsarjan nimi?'), sg.Text('', key='_OUTPUT2_', text_color=('blue')) ],
              [sg.Input(size=(40,3),do_not_clear=False, key='_IN2_')],
              [sg.Image('villelogo.png')],
              [sg.Output(size=(40,30))],
              [sg.Button('OK', button_color=('white','green')),sg.Button('F11'),sg.Button('Start'),sg.Exit(button_color=('white','red')),sg.Text('          by Epi')]]


    window = sg.Window('VILLEbot v1.0',auto_size_text=False, default_element_size=(20,1), keep_on_top = True).Layout(layout)
    window.SetIcon('favicon.ico')


    while True:
        event, values = window.Read(timeout=0)
        if event is None or event == 'Exit':
            break
        if event == 'F11':
            pyautogui.moveRel(-100,0)
            pyautogui.click()
            pyautogui.press('f11')
            pyautogui.moveRel(100,0)
        if event == 'OK':
            try:
                questions = int(values['_IN_'])
                for i in range(questions):
                    wrong.append([])
            except ValueError:
                print("Yritätkö edes? Anna numero!")
            assignmentName = str(values['_IN2_'])
            window.FindElement('_OUTPUT_').Update(values['_IN_'])
            window.FindElement('_OUTPUT2_').Update(values['_IN2_'])
        if event == 'Start':
            while (len(correctAnswers)) < questions:
                for i in range(5):
                    pyautogui.press('pgdn')
                pos = None
                done = False
                print("\nTehtävä numero: ",task+1)
                print("Oikeita vastauksia kerätty: ",len(correctAnswers),"\n")
                window.Read(timeout=0)
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
                            window.Read(timeout=0)
                            if len(correctAnswers) > task:
                                for i in range(len(texts)):
                                    if (texts[i] in correctAnswers[task]):
                                        pyautogui.click(locations[i])
                                        window.Read(timeout=0)
                                        done = True
                    texts = []
                    locations = []
                    window.Read(timeout=0)
                while True:
                    if last[-1] in wrong[task]:
                        pass
                        if last[-2] in wrong[task]:
                            pass
                            if last[-3] in wrong[task]:
                                pass
                                if last[-4] in wrong[task]:
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

                    window.Read(timeout=0)

                    # findGreen = pyautogui.locateOnScreen('green.png')
                    # findGreen2 = pyautogui.locateOnScreen('green3.png')
                    # if findGreen is None:
                    #     pyautogui.locateOnScreen('green3.png')
                    # else:
                    #     pyautogui.locateOnScreen('green.png')


                    if pyautogui.locateOnScreen('green.png') != None:

                        for i in range(5):
                            pyautogui.press('pgdn')
                        task += 1
                        if len(correctAnswers) >= (task):
                            next2 = pyautogui.locateCenterOnScreen('next2.png')
                            next = pyautogui.locateCenterOnScreen('next.png')
                            if next is None:
                                pyautogui.click(next2)
                            else:
                                pyautogui.click(next)
                            for i in range(5):
                                pyautogui.press('pgdn')
                            #time.sleep(0.5)
                            window.Read(timeout=0)
                            break
                        else:
                            print("\nOikea vastaus:")
                            print(last[-1],"\n")
                            #wrong = []
                            x = pyautogui.locateCenterOnScreen('x.png')
                            if x is not None:
                                pyautogui.click(pyautogui.locateCenterOnScreen('x.png'))
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
                            #time.sleep(0.5)
                            window.Read(timeout=0)
                            break

                    if pyautogui.locateOnScreen('green.png') == None:
                        # if len(wrong) > 5:
                        #     wrong = []
                        print("\nVäärä vastaus:")
                        print(n,"\n")
                        wrong[task].append(n)
                        print("\nArvattu ",len(wrong[task])," kertaa tehtävää numero",len(correctAnswers)+1,"\n")
                        task = 0
                        x = pyautogui.locateCenterOnScreen('x.png')
                        if x is not None:
                            pyautogui.click(pyautogui.locateCenterOnScreen('x.png'))
                        pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
                        window.Read(timeout=0)
                        for i in range(5):
                            pyautogui.press('pgdn')
                        break

            print("Oikeat vastaukset: ")
            nr = 1
            for i in correctAnswers:
                print(nr,": ",i)
                nr += 1
            nr = 1
            with open("vastaukset.txt", "a", encoding='utf-8') as f:
                f.write("\n" + str(assignmentName) + "\n")
                for i in correctAnswers:
                    f.write(str(nr) + ": " + str(i) + "\n")
                    nr += 1
            window.Read(timeout=0)
            texts = []
            locations = []
            choices = []
            last = ['none','none','none','none','none']
            wrong = []
            correctAnswers = []
            task = 0
    window.Close()
main()
