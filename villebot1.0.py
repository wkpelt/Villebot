#VILLEBot v1.0
#Author = Wiljam Peltomaa
#Last updated = 19.11.2018
import PySimpleGUI as sg
import pyautogui
import pyperclip
import string
import time

def main():
    print('Press Ctrl-Alt-Del to stop the bot.')
    texts = []
    locations = []
    choices = []
    last = []
    correct_answers = []
    wrong = []
    task = 0
    questions = 0
    assignment_name = "Tehtävä"

    layout = [[sg.Text('Montako kysymystä?'),
               sg.Text('', key='_OUTPUT_', text_color='blue', background_color='white', size=(17, 1))],
              [sg.Input(size=(40, 3), do_not_clear=False, key='_IN_')],
              [sg.Text('Tehtäväsarjan nimi?'),
               sg.Text('', key='_OUTPUT2_', text_color='blue', background_color='white', size=(17, 1))],
              [sg.Input(size=(40, 3), do_not_clear=False, key='_IN2_')],
              [sg.Image('villelogo.png')],
              [sg.Output(size=(37, 30))],
              [sg.Text('Tehtävä nr:', size=(8, 1)), sg.Text('', key='_OUTPUT3_', size=(2, 1))],
              [sg.Text('Kerättyjä vastauksia:', size=(15, 1)), sg.Text('', key='_OUTPUT4_', size=(2, 1))],
              [sg.Button('OK', button_color=('white', 'green')), sg.Button('F11'), sg.Button('Start'),
               sg.Text('by Epi', size=(12, 1)), sg.Exit(button_color=('white', 'red'), size=(5, 1)), ]]

    window = sg.Window('VILLEbot v1.0', auto_size_text=False, default_element_size=(16, 1), keep_on_top=True).Layout(
        layout)
    window.SetIcon('favicon.ico')

    while True:
        event, values = window.Read(timeout=0)
        if event is None or event == 'Exit':
            break
        if event == 'F11':
            pyautogui.moveRel(-100, 0)
            pyautogui.click()
            pyautogui.press('f11')
            pyautogui.moveRel(100, 0)
        if event == 'OK':
            try:
                questions = int(values['_IN_'])
                for i in range(questions):
                    wrong.append([])
            except ValueError:
                print("Yritätkö edes? Anna numero!")
            assignment_name = str(values['_IN2_'])
            window.FindElement('_OUTPUT_').Update(values['_IN_'])
            window.FindElement('_OUTPUT2_').Update(values['_IN2_'])
        if event == 'Start':
            restart = pyautogui.locateCenterOnScreen('restart.png')
            while (len(correct_answers)) < questions:
                for i in range(5):
                    pyautogui.press('pgdn')
                pos = None
                done = False

                window.FindElement('_OUTPUT3_').Update(task + 1)
                window.FindElement('_OUTPUT4_').Update(len(correct_answers))
                window.Read(timeout=0)

                while pos is None:
                    for pos in pyautogui.locateAllOnScreen('blue3.png',grayscale=True):
                        if not done:
                            pyautogui.moveTo(pos[0] - 20, pos[1] + 5)
                            pyautogui.dragRel(700, 45, 0.2, button='left')
                            pyautogui.hotkey('ctrl', 'c')
                            copied_text = pyperclip.paste()
                            copied_text.strip("\r\n")
                            texts.append(copied_text)
                            last.append(copied_text)
                            locations.append((pos[0] + 5, pos[1] + 5))
                            choices.append((pos[0] + 5, pos[1] + 5))
                            window.Read(timeout=0)
                            if len(correct_answers) > task:
                                for i in range(len(texts)):
                                    if texts[i] in correct_answers[task]:
                                        pyautogui.click(locations[i])
                                        window.Read(timeout=0)
                                        done = True
                            else:
                                for i in range(len(texts)):
                                    if texts[i] not in wrong[task]:
                                        pyautogui.click(locations[i])
                                        window.Read(timeout=0)
                                        done = True
                    texts = []
                    locations = []
                    window.Read(timeout=0)

                while True:
                    window.Read(timeout=0)
                    if (questions == (task+1)):
                        time.sleep(0.1)
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('enter')

                    green = pyautogui.locateOnScreen('green.png')
                    if green is not None:
                        task += 1
                        if len(correct_answers) >= task:
                            pyautogui.press('enter')
                            for i in range(5):
                                pyautogui.press('pgdn')
                            window.Read(timeout=0)
                            break
                        else:
                            print("Oikea vastaus:")
                            print(last[-1], "\n")
                            #pyautogui.moveTo(green[0], green[1])
                            #pyautogui.dragRel(700, 45, 0.2, button='left')
                            #pyautogui.hotkey('ctrl', 'c')
                            #right_answer = pyperclip.paste()
                            right_answer = last[-1]
                            correct_answers.append(right_answer.strip("\r\n"))
                            pyautogui.press('enter')
                            for i in range(5):
                                pyautogui.press('pgdn')
                            window.Read(timeout=0)
                            break

                    elif green is None:
                        print("Väärä vastaus:")
                        print(last[-1], "\n")
                        wrong[task].append(last[-1])
                        print("Arvattu ", len(wrong[task]), " kertaa tehtävää numero", len(correct_answers) + 1, "\n")
                        task = 0
                        pyautogui.click(restart)
                        #pyautogui.click(pyautogui.locateCenterOnScreen('restart.png',grayscale=True))
                        window.Read(timeout=0)
                        for i in range(5):
                            pyautogui.press('pgdn')
                        break

            print("Oikeat vastaukset: ")
            nr = 1
            with open("vastaukset.txt", "a", encoding='iso-8859-1') as f:
                f.write("\n" + str(assignment_name) + "\n")
                for i in correct_answers:
                    f.write(str(nr) + ": " + str(i) + "\n")
                    print(nr, ": ", i)
                    nr += 1
            window.Read(timeout=0)
            texts = []
            locations = []
            choices = []
            last = []
            wrong = []
            correct_answers = []
            task = 0
    window.Close()

main()
