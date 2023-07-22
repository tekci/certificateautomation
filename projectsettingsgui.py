import PySimpleGUI as sg
from methods import select_file, getDemoImage, resize_image

def Settings(config):
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
                [sg.Text('X-Center:'), sg.InputText(default_text=dx)],
                [sg.Text('Y-Center:'), sg.InputText(default_text=dy)],
                [sg.Text('Font Path:'), sg.InputText(default_text=dfontpath, key='-FONT_PATH-')],
                [sg.Button('Chose Font')],
                [sg.Text('Font Size:'), sg.InputText(default_text=dfontsize)],
                [sg.Text('Red:'), sg.InputText(default_text=dred)],
                [sg.Text('Green:'), sg.InputText(default_text=dgreen)],
                [sg.Text('Blue:'), sg.InputText(default_text=dblue)],
                [sg.Text('Opacity:'), sg.InputText(default_text=dopacity)],
                [sg.Button('Save'), sg.Button('Cancel'), sg.Button('See Demo')]]

    # Create the Window
    window = sg.Window('Project Settings', layout)
    new_settings = []
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        print(values)
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        elif event == 'Save':
            new_settings = [values[0], values[1], values['-CERT_PATH-'].replace("\\\\", '/'), values['-FONT_PATH-'].replace("\\\\", '/'), values[2], f"{values[3]}, {values[4]}, {values[5]}, {values[6]}"]
            break
        elif event == "Chose Certificate":
            window.Element('-CERT_PATH-').Update(select_file())
        elif event == "Chose Font":
            window.Element('-FONT_PATH-').Update(select_file())
        elif event == "See Demo":
            demo_image = getDemoImage([values[0], values[1], values['-CERT_PATH-'].replace("\\\\", '/'), values['-FONT_PATH-'].replace("\\\\", '/'), values[2], f"{values[3]}, {values[4]}, {values[5]}, {values[6]}"])
            demo_image = resize_image(demo_image, 300)
            window["-IMAGE-"].update(data=demo_image)

    window.close()
    return new_settings
