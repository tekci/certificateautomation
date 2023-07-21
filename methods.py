from PIL import Image, ImageDraw, ImageFont
import os

# Modify these fields for your usecase
certificate_file_path = os.getcwd() + "/EMPTY.png"
output_file_path = os.getcwd() + '/output'

x_center = 1190
y_center = 930

font_path = "segoeuibold.ttf"
font_size = 150
color = (0,0,0,255) # R G B Opacity


def createCertificate(name):
    output_path = output_file_path + f'/certificate-{name}.png'
    font_color = (255, 0, 0)  # RGB color (red in this example)

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
    image.save(output_path)






