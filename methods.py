from PIL import Image, ImageDraw, ImageFont

certificate_file_path = "C:/Users/YUSUF/PycharmProjects/certificateautomation/img.png"

def getNames():
    nameslist = []

    userinput = ""

    exit = ['done', " "]
    while not userinput.lower() in exit:
        userinput = input("Enter names separated by a comma , enter done to submit: ")
        for name in userinput.split(','):
            if not userinput.lower() in exit:
                nameslist.append(name)
    return nameslist

def creatPDF(namesList):
    for name in namesList:
        output_path = f'C:/Users/YUSUF/PycharmProjects/certificateautomation/output/certificate-{name}.png'
        font_color = (255, 0, 0)  # RGB color (red in this example)

        # Open the image
        image = Image.open(certificate_file_path)

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("arial.ttf", 75)

        text_width, text_height = font.getsize(name)

        # Calculate the position to center the text
        x_position = 650 - text_width// 2
        y_position = 500 - text_height// 2
        position = (x_position, y_position)

        # Draw the text on the image
        draw.text(position, name, font=font, fill=(0,0,0,255))

        # Save the modified image to a new file
        image.save(output_path)






