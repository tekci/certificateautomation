import PySimpleGUI as sg
from methods import select_file, getDemoImage, resize_image

def Settings(config, name):
    dcertpath = ""
    dx = 0
    dy = 0
    dfontpath = ""
    dfontsize = 100
    dred = 0
    dgreen = 0
    dblue = 0
    dopacity = 255
    if config != None:
        try:
            dcertpath = config[2].strip()
            dx = int(config[0].strip())
            dy = int(config[1].strip())
            dfontpath = config[3].strip()
            dfontsize = int(config[4].strip())
            colors = config[5].split(' ')
            dred = colors[0].strip(',')
            dgreen = colors[1].strip(',')
            dblue = colors[2].strip(',')
            dopacity = colors[3].strip(',')
        except Exception:
            pass

    sg.theme('DarkAmber')   # Add a touch of color
    # All the stuff inside your window.
    layout = [  [sg.Image(key="-IMAGE-", size=(300, 300))],
                [sg.Text('Certificate Path:'), sg.InputText(default_text=dcertpath, key='-CERT_PATH-')],
                [sg.Button('Chose Certificate')],
                [sg.Text('X-Center:'), sg.InputText(default_text=dx, key='-X_CENTER-')],
                [sg.Text('Y-Center:'), sg.InputText(default_text=dy, key='-Y_CENTER-')],
                [sg.Text('Font Path:'), sg.InputText(default_text=dfontpath, key='-FONT_PATH-')],
                [sg.Button('Chose Font')],
                [sg.Text('Font Size:'), sg.InputText(default_text=dfontsize, key='FONT_SIZE')],
                [sg.Text('Red:'), sg.InputText(default_text=dred, key='RED')],
                [sg.Text('Green:'), sg.InputText(default_text=dgreen, key='GREEN')],
                [sg.Text('Blue:'), sg.InputText(default_text=dblue, key='BLUE')],
                [sg.Text('Opacity:'), sg.InputText(default_text=dopacity)],
                [sg.Button('Save'), sg.Button('Cancel'), sg.Button('See Demo')]]

    # Create the Window
    window = sg.Window(f'Project Settings | {name}', layout)
    new_settings = []
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(values)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        elif event == 'Save':
            new_settings = [values["-X_CENTER-"], values["-Y_CENTER-"], values['-CERT_PATH-'].replace("\\\\", '/'), values['-FONT_PATH-'].replace("\\\\", '/'), values["FONT_SIZE"], f"{values['RED']}, {values['GREEN']}, {values['BLUE']}, {values[0]}"]
            break
        elif event == "Chose Certificate":
            window.Element('-CERT_PATH-').Update(select_file())
        elif event == "Chose Font":
            window.Element('-FONT_PATH-').Update(select_file())
        elif event in ["-CERT_PATH-", "-X_CENTER-", "-Y_PATH-", "-FONT_PATH-", "FONT_SIZE", "RED", "GREEN", "BLUE", "See Demo"]:
            demo_image = getDemoImage([values["-X_CENTER-"], values["-Y_CENTER-"], values['-CERT_PATH-'].replace("\\\\", '/'), values['-FONT_PATH-'].replace("\\\\", '/'), values["FONT_SIZE"], f"{values['RED']}, {values['GREEN']}, {values['BLUE']}, {values[0]}"])
            demo_image = resize_image(demo_image, 400)
            window["-IMAGE-"].update(data=demo_image)

    window.close()
    return new_settings
