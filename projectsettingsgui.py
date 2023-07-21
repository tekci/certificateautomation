import PySimpleGUI as sg

def Settings(config):
    if config == None:
        dcertpath = ""
        dx = 0
        dy = 0
        dfontpath = ""
        dfontsize = 100
        dred = 0
        dgreen = 0
        dblue = 0
        dopacity = 255
    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Text('Certificate Path:'), sg.InputText(default_text=dcertpath)],
                [sg.Text('X-Center:'), sg.InputText(default_text=dx)],
                [sg.Text('Y-Center:'), sg.InputText(default_text=dy)],
                [sg.Text('Font Path:'), sg.InputText(default_text=dfontpath)],
                [sg.Text('Font Size:'), sg.InputText(default_text=dfontsize)],
                [sg.Text('Red:'), sg.InputText(default_text=dred)],
                [sg.Text('Green:'), sg.InputText(default_text=dgreen)],
                [sg.Text('Blue:'), sg.InputText(default_text=dblue)],
                [sg.Text('Opacity:'), sg.InputText(default_text=dopacity)],
                [sg.Button('Save'), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        print('You entered ', values[0])

    window.close()

Settings(None)