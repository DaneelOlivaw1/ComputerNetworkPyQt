import PySimpleGUI as sg

sg.theme('SystemDefault')
sg.set_options(font="Helvetica 15")
ComputerList = ["A", "B", "C"]


# All the stuff inside your window.
layout = [[sg.Text('A', background_color='#d3dfda', justification='center', size=(7, 3))],
          [sg.Text('A', background_color='#d3dfda',
                   justification='center', size=(7, 3))],
          [sg.Text('B', background_color='#d3dfda',
                   justification='center', size=(7, 3))],
          [sg.Text('从哪个计算机发送'), sg.InputCombo((ComputerList), size=(4, 1)),
           sg.Text('要发送到哪个计算机'), sg.InputCombo((ComputerList), size=(4, 1))],
          [sg.Text('要发送的数据'), sg.InputText()],
          [sg.Button('Send'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    print('You entered ', values[0])

window.close()
