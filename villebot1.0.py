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
    last = ''
    correct_answers = []
    wrong = []
    task = 0
    questions = 0
    assignment_name = "Tehtävä"
    allDone = False

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

    def scrollDown():
        for i in range(5):
            pyautogui.press('pgdn')

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

            while allDone is False:
                scrollDown()
                done = False

                window.FindElement('_OUTPUT3_').Update(task + 1)
                window.FindElement('_OUTPUT4_').Update(len(correct_answers))
                window.Read(timeout=0)

                for pos in pyautogui.locateAllOnScreen('blue3.png'):
                    if not done:
                        locations.append((pos[0] + 5, pos[1] + 5))
                        if len(correct_answers) > task and len(correct_answers) != questions:
                            pyautogui.click(locations[-1])
                            window.Read(timeout=0)
                            done = True
                        else:
                            pyautogui.moveTo(pos[0] - 20, pos[1] + 5)
                            pyautogui.dragRel(700, 45, 0.2, button='left')
                            pyautogui.hotkey('ctrl', 'c')
                            copied_text = pyperclip.paste()
                            texts.append(copied_text.strip("\r\n"))
                            last = copied_text.strip("\r\n")
                            window.Read(timeout=0)
                            if len(correct_answers) == questions:
                                if correct_answers[task] == last:
                                    pyautogui.click(locations[-1])
                                    pyautogui.press('enter')
                                    if task+1 == questions:
                                        allDone = True
                                    task += 1
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

                while len(correct_answers) != questions:
                    window.Read(timeout=0)
                    if (questions == (task+1)):
                        time.sleep(0.1)
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('tab')
                        time.sleep(0.1)
                        pyautogui.press('enter')

                    if len(correct_answers) > task:
                            pyautogui.press('enter')
                            task += 1
                            print("Skip\n")
                            break

                    green = pyautogui.locateOnScreen('green.png')
                    if green is not None:
                        task += 1
                        if len(correct_answers) >= task:
                            pyautogui.press('enter')
                            scrollDown()
                            window.Read(timeout=0)
                            break
                        else:
                            print("Oikea vastaus:")
                            print(last, "\n")
                            right_answer = last
                            correct_answers.append(right_answer.strip("\r\n"))
                            pyautogui.press('enter')
                            scrollDown()
                            window.Read(timeout=0)
                            if len(correct_answers) == questions:
                                pyautogui.click(restart)
                                task = 0
                            break

                    elif green is None:
                        print("Väärä vastaus:")
                        print(last, "\n")
                        wrong[task].append(last)
                        print("Arvattu ", len(wrong[task]), " kertaa tehtävää numero", len(correct_answers) + 1, "\n")
                        task = 0
                        pyautogui.click(restart)
                        window.Read(timeout=0)
                        scrollDown()
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
            last = ''
            wrong = []
            correct_answers = []
            task = 0
            pyautogui.alert(text='Valmis!', title='', button='OK')
    window.Close()

main()
