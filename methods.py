from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import os
from datetime import datetime
from pdf2image import convert_from_path


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

def select_font():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Show the directory selector dialog and store the selected path
    selected_file = filedialog.askopenfilename(initialdir=os.getcwd()+'/fonts')

    # Return the selected directory path
    return selected_file

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
    try:
        image = Image.open(certificate_file_path)
    except Exception as e:
        image = convert_from_path(certificate_file_path)[0]



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

def getDemoImage(config):
    certificate_file_path = config[2].strip()

    x_center = int(config[0].strip())
    y_center = int(config[1].strip())

    font_path = config[3].strip()
    font_size = int(config[4].strip())
    colorList = []
    for item in config[5].split(' '):
        colorList.append(int(item.strip(',')))
    color = tuple(colorList)

    try:
        image = Image.open(certificate_file_path)
    except Exception:
        image = convert_from_path(certificate_file_path)[0]

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = font.getsize("John Smith")

    # Calculate the position to center the text
    x_position =  x_center - text_width// 2
    y_position =  y_center - text_height// 2
    position = (x_position, y_position)

    # Draw the text on the image
    draw.text(position, "John Smith", font=font, fill=color)

    # Convert the PIL Image object to bytes using BytesIO
    image_bytes = BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    # Return the bytes-like object containing the image data
    return image_bytes.read()

def resize_image(image_data, desired_width):
    image = Image.open(BytesIO(image_data))
    image.thumbnail((desired_width, image.size[1]))

    # Convert the resized PIL Image object to bytes using BytesIO
    resized_image_bytes = BytesIO()
    image.save(resized_image_bytes, format="PNG")
    resized_image_bytes.seek(0)

    return resized_image_bytes.read()




