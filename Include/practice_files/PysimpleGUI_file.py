import PySimpleGUI as sg

layout = [[sg.Text('Enter the first number:'), sg.InputText()],
          [sg.Text('Enter the second number:'), sg.InputText()],
          [sg.Button('Add'), sg.Button('Cancel')]]

window = sg.Window('Add Two Numbers', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        num1 = int(values[0])
        num2 = int(values[1])
        result = num1 + num2
        sg.popup(f'The sum of {num1} and {num2} is {result}')
    except ValueError:
        sg.popup('Please enter valid integers')

window.close()





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
