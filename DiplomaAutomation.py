from PIL import ImageDraw, Image, ImageFont
import time
import random
import os

name_in_file = "names.txt"
lastname_in_file = "lastnames.txt"
diploma_image_in_file = "diploma.jpg"
output_path = "./out"


######

def diploma(text, path, template):
    im = Image.open(template)

    d = ImageDraw.Draw(im)
    font = ImageFont.truetype("BELL.ttf", 22)

    d.text((im.size[0] / 2, 145), text, fill="black", anchor="ms", font=font)

    #im.show()
    im.save(path + "/" + text.replace(" ", "_") + ".jpg")

######

def startAutomation(path, template, name_file, last_name_file = ""):

    if not os.path.exists(path):
        os.makedirs(path)

    last_name_exists = False if last_name_file == "" else False

    name_list = open(name_file).readlines()
    last_name_list = open(last_name_file).readlines() if last_name_exists else [""]

    start = time.time_ns()

    i = 0
    maxiteration = 50

    for name_line in name_list:
        i += 1
        if i == maxiteration + 1:
            break

        last_name_index = random.randint(0, len(last_name_list) - 1)

        name = name_line[:-1].lower().title()
        last_name = last_name_list[last_name_index][:-1].lower().title() if last_name_exists else ""

        fullname = f"{name} {last_name}" if last_name_exists else name

        #print(i[:-1])
        diploma(fullname, path, template)

        print(f"[{i} : {maxiteration}] - {fullname}")

    print((time.time_ns() - start) * (10 ** -9))

startAutomation(output_path, diploma_image_in_file, name_in_file, lastname_in_file)
