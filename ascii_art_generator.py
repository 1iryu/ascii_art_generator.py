from dataclasses import replace
import cv2
import math
import subprocess


#input img -> convert to gray frame -> resize -> convert to ascii -> format text file -> output as text file -> open text file
def make_ascii_image(input_path: str, output_path: str,size : int):
    img = cv2.imread(input_path)
    grayFrame = convert_to_gray_scale(img)
    grayFrame = resize_image(grayFrame, size)
    ascii_img = return_ascii_image(grayFrame)
    ascii_img = convert_ascii_img_to_text(ascii_img)
    output_as_text_file(ascii_img, output_path)
    open_notepad(output_path)


def get_ascii_by_average(num: int):
    length = len(grayRamp) - 1
    index = math.ceil(length/255 * num)
    char = grayRamp[index]
    return char


def return_ascii_image(image):
    height, width = image.shape
    ascii_image = [[""] * width for _ in range(height)]
    for i in range(height):
        for j in range(width):
            rgb = int(image[i][j])
            char = get_ascii_by_average(rgb)
            ascii_image[i][j] = char
    return ascii_image


def convert_to_gray_scale(frame):
    return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


def convert_ascii_img_to_text(ascii_img):
    text = ""
    for i in range(len(ascii_img)):
        if(i != 0):
            text += "\n"
        for j in range(len(ascii_img[i])):
            text += ascii_img[i][j]
    return text


def resize_image(image_frame, new_width):
    height, width = image_frame.shape
    ratio = (height / float(width * 2.5))
    new_height = int(new_width * ratio)
    frame = cv2.resize(image_frame, (new_width, new_height))
    return frame


def output_as_text_file(ascii_img,output_path : str):
    f = open(output_path, 'a', encoding='UTF-8')
    f.write(ascii_img)
    f.close()


def open_notepad(path : str):
    subprocess.Popen(['notepad.exe', path])



