import PySimpleGUI as sg

layout=[[sg.Text(text="Hello world",justification='center')],
        [sg.Button('click')]]
window=sg.Window("Trial",layout,size=(200,100))
while True:
    event,value=window.read()
    # print(event,value)
    if event in (None,'Exit'):
        break
    if event=='click':
        # sg.popup('ok')
        # fl=open('D:/python programs/All/.venv/Include/practice_files/temp.txt')
        # txt=fl.read()
        # print( sg.popup_scrolled(txt))
        # print( sg.popup_get_file(txt,  title="File selector"))
        # fl.close()
        # sg.popup_auto_close('This window will Autoclose')

        choices = ['Choice 1', 'Choice 2', 'Choice 3']
        combo = sg.Combo(choices, default_value='Choice 1')
        

window.close()








# layout = [[sg.Text('Enter the first number:'), sg.InputText()],
#           [sg.Text('Enter the second number:'), sg.InputText()],
#           [sg.Button('Add'), sg.Button('Cancel')]]

# window = sg.Window('Add Two Numbers', layout)

# while True:
#     event, values = window.read()
#     if event in (None, 'Cancel'):
#         break
#     try:
#         num1 = int(values[0])
#         num2 = int(values[1])
#         result = num1 + num2
#         sg.popup(f'The sum of {num1} and {num2} is {result}')
#     except ValueError:
#         sg.popup('Please enter valid integers')

# window.close()





# import PySimpleGUI as sg

# layout = [[sg.Text("Click the button to change the text")],
#           [sg.Button("Click me!")],
#           [sg.Text(size=(30, 1), key="-OUTPUT-")]]

# window = sg.Window("My First GUI", layout)

# while True:
#     event, values = window.read()
#     if event == "Click me!":
#         window["-OUTPUT-"].update("Hello World!")
#     if event == sg.WIN_CLOSED:
#         break

# window.close()
