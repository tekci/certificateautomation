from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d-%m-%Y-%H-%M")

import tkinter as tk
from tkinter import filedialog

def select_directory():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the directory selector dialog and store the selected path
    selected_directory = filedialog.askdirectory()

    # Return the selected directory path
    return selected_directory

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the directory selector dialog and store the selected path
    selected_file = filedialog.askopenfilename()

    # Return the selected directory path
    return selected_file

def createCertificate(name, config, path):
    certificate_file_path = config[2].strip()

    output_file_path = path + f'/output'

    if not os.path.exists(output_file_path):
        os.mkdir(output_file_path)

    x_center = int(config[0].strip())
    y_center = int(config[1].strip())

    font_path = config[3].strip()
    font_size = int(config[4].strip())
    colorList = []
    for item in config[5].split(' '):
        colorList.append(int(item.strip(',')))
    color = tuple(colorList)

    # Open the image
    image = Image.open(certificate_file_path)

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = font.getsize(name)

    # Calculate the position to center the text
    x_position =  x_center - text_width// 2
    y_position =  y_center - text_height// 2
    position = (x_position, y_position)

    # Draw the text on the image
    draw.text(position, name, font=font, fill=color)

    # Save the modified image to a new file
    image.save(output_file_path+f'/{dt_string}_{name}.png')





