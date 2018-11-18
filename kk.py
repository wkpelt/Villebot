import pyautogui,sys
import time
import pyperclip
import string
import PySimpleGUI as sg

def main():

    print('Press Ctrl-Alt-Del to stop the bot.')
    texts = []
    locations = []
    choices = []
    last = ['none','none','none','none','none']
    wrong = []
    correctAnswers = []
    task = 0
    start = False


    layout = [[sg.Text('Montako kysymystä?'), sg.Text('', key='_OUTPUT_') ],
              [sg.Input(size=(40,3),do_not_clear=False, key='_IN_')],
              [sg.Checkbox('F11', size=(10,1), key='_F11_')],
              [sg.Text('', key='_STUFF_',size=(40, 3))],
              [sg.Output(size=(40,30))],
              [sg.Button('OK'),sg.Button('Start'),sg.Button('Pause'),sg.Button('Unpause'),sg.Exit()]]


    window = sg.Window('VILLEbot v0.9',auto_size_text=True, keep_on_top = True).Layout(layout)
    window.SetIcon('favicon.ico')


    while True:
        event, values = window.Read(timeout=0)
        if event is None or event == 'Exit':
            break
        if values['_F11_']:
            #pyautogui.press('f11')
            pass
        if event == 'OK':
            questions = int(values['_IN_'])
            window.FindElement('_OUTPUT_').Update(values['_IN_'])
            #window.FindElement('_STUFF_').Update(values['_IN_'])
            #sg.Print(values['_IN_'],keep_on_top = True)
        if event == 'Start':
            while (len(correctAnswers)) < questions-1:
                #time.sleep(0.2)
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

                    # print("Correct answers: ",correctAnswers)
                    # print("Wrong answers: ",wrong)
                    texts = []
                    locations = []
                    window.Read(timeout=0)

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
                            #time.sleep(0.5)
                            window.Read(timeout=0)
                            break

                    if pyautogui.locateOnScreen('green.png') == None:
                        if len(wrong) > 5:
                            wrong = []
                        task = 0
                        print("\nVäärä vastaus:")
                        print(n,"\n")
                        wrong.append(n)
                        pyautogui.click(pyautogui.locateCenterOnScreen('restart.png'))
                        print("\nArvattu ",len(wrong)," kertaa tehtävää numero",len(correctAnswers)+1,"\n")
                        window.Read(timeout=0)
                        for i in range(5):
                            pyautogui.press('pgdn')
                        break

            print("Oikeat vastaukset: ")
            nr = 1
            for i in correctAnswers:
                print(nr,": ",i)
                nr += 1
            while True:
                window.Read(timeout=0)
    window.Close()
main()
