#VILLEBot v1.0
#Author = Wiljam Peltomaa
#Last updated = 21.04.2019
import PySimpleGUI as sg
import pyautogui
import pyperclip
import string
from time import sleep

def main():
    print('To stop the bot, drag the cursor to the top-left corner of your screen or press Ctrl-Alt-Del')
    texts = []
    locations = []
    last = ''
    correct_answers = []
    wrong = []
    task = 0
    questions = 0
    assignment_name = "Tehtävä" #default name
    allDone = False

    #GUI
    layout = [[sg.Text('Montako kysymystä?'),
               sg.Text('', key='total_questions', text_color='blue', background_color='white', size=(17, 1))],
              [sg.Input(size=(40, 3), do_not_clear=False, key='_IN_')],
              [sg.Text('Tehtäväsarjan nimi?'),
               sg.Text('', key='assignment_name', text_color='blue', background_color='white', size=(17, 1))],
              [sg.Input(size=(40, 3), do_not_clear=False, key='_IN2_')],
              [sg.Image('villelogo.png')],
              [sg.Output(size=(37, 30))],
              [sg.Text('Tehtävä nr:', size=(8, 1)), sg.Text('', key='current_task', size=(2, 1))],
              [sg.Text('Kerättyjä vastauksia:', size=(15, 1)), sg.Text('', key='collected_answers', size=(2, 1))],
              [sg.Button('OK', button_color=('white', 'green')), sg.Button('F11'), sg.Button('Start'),
               sg.Text('by wkpelt', size=(12, 1)), sg.Exit(button_color=('white', 'red'), size=(5, 1)), ]]

    window = sg.Window('VILLEbot v1.0', auto_size_text=False, default_element_size=(16, 1), keep_on_top=True).Layout(layout)
    window.SetIcon('favicon.ico')

    def scrollDown(n):
        for i in range(n):
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
            window.FindElement('total_questions').Update(values['_IN_'])
            window.FindElement('assignment_name').Update(values['_IN2_'])
        if event == 'Start':
            #find restart button on screen
            restart = pyautogui.locateCenterOnScreen('restart.png')

            while allDone is False:
                scrollDown(5)
                #update values on gui
                window.FindElement('current_task').Update(task + 1)
                window.FindElement('collected_answers').Update(len(correct_answers))
                window.Read(timeout=0)

                done = False

                #find the x,y positions of all possible answers on screen
                for pos in pyautogui.locateAllOnScreen('blue.png'):
                    if not done:
                        locations.append((pos[0] + 5, pos[1] + 5))

                        #skip if the correct answer for the current task has already been found
                        if len(correct_answers) > task and len(correct_answers) != questions:
                            pyautogui.click(locations[-1])
                            done = True

                        #else scan the whole page
                        else:
                            pyautogui.moveTo(pos[0] - 20, pos[1] + 5)
                            pyautogui.dragRel(700, 45, 0.2, button='left')
                            pyautogui.hotkey('ctrl', 'c')
                            copied_text = pyperclip.paste()
                            texts.append(copied_text.strip("\r\n"))
                            last = copied_text.strip("\r\n")

                            #if all the correct answers have been found
                            if len(correct_answers) == questions:
                                if correct_answers[task] == last:
                                    pyautogui.click(locations[-1])
                                    pyautogui.press('enter')
                                    if task+1 == questions:
                                        allDone = True
                                    task += 1
                                    done = True

                            #check if last copied text has already been tried before
                            else:
                                for i in range(len(texts)):
                                    if texts[i] not in wrong[task]:
                                        pyautogui.click(locations[i])
                                        done = True
                    texts = []
                    locations = []
                    window.Read(timeout=0)

                while len(correct_answers) != questions:
                    window.Read(timeout=0)

                    #if the current question is the last question, get rid of the popup
                    if (questions == (task+1)):
                        sleep(0.1)
                        pyautogui.press('tab', interval=0.1)
                        pyautogui.press('tab', interval=0.1)
                        pyautogui.press('enter', interval=0.1)

                    #if the current question's correct answer has already been found, skip
                    if len(correct_answers) > task:
                            pyautogui.press('enter')
                            task += 1
                            print("Skip\n")
                            break

                    green = pyautogui.locateOnScreen('green.png')

                    #if clicked option was the correct answer
                    if green is not None:
                        task += 1
                        #skip if found already
                        if len(correct_answers) >= task:
                            pyautogui.press('enter')
                            scrollDown(5)
                            window.Read(timeout=0)
                            break
                        #new correct answer
                        else:
                            print(f"Oikea vastaus:\n {last} \n")
                            right_answer = last
                            #strip unnecessary regex from the copied text (ty ville)
                            correct_answers.append(right_answer.strip("\r\n"))
                            pyautogui.press('enter')
                            scrollDown(5)
                            window.Read(timeout=0)
                            if len(correct_answers) == questions:
                                pyautogui.click(restart)
                                task = 0
                            break

                    #if clicked option was the wrong answer
                    elif green is None:
                        print(f"Väärä vastaus:\n {last} \n")
                        wrong[task].append(last)
                        print("Arvattu ", len(wrong[task]), " kertaa tehtävää numero", len(correct_answers) + 1, "\n")
                        task = 0
                        pyautogui.click(restart)
                        window.Read(timeout=0)
                        scrollDown(5)
                        break

            print("Oikeat vastaukset: ")
            #save the correct answers into a .txt file
            nr = 1
            with open("vastaukset.txt", "a", encoding='iso-8859-1') as f:
                f.write("\n" + str(assignment_name) + "\n")
                for i in correct_answers:
                    f.write(str(nr) + ": " + str(i) + "\n")
                    print(nr, ": ", i)
                    nr += 1
            window.Read(timeout=0)
            #clear the variables
            wrong = []
            correct_answers = []
            task = 0
            questions = 0
            allDone = False
            #alert that all the correct answers have been found
            pyautogui.alert(text='Valmis!', title='', button='OK')
    window.Close()

main()
