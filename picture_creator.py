import argparse
from PIL import Image, ImageDraw
from random import randint
from datetime import datetime

FILE = 'timers'
TYPE = 1
XSIZE = 30000
YSIZE = 15000

parser = argparse.ArgumentParser(description='Picture generation')
parser.add_argument('--dest', action='store', type=str, default=FILE,
                    help='output filename, string')
parser.add_argument('--type', action='store', type=int, default=TYPE,
                    help="""type of file content:
                    0 - Empty,
                    1 - Noise,
                    2 - Gradient""")
parser.add_argument('--xsize', action='store', type=int, default=XSIZE,
                    help='horizontal size of image')
parser.add_argument('--ysize', action='store', type=int, default=YSIZE,
                    help='vertical size of image')

arguments = parser.parse_args()
filename = arguments.dest
content = arguments.type
x_size = arguments.xsize
y_size = arguments.ysize


def percent_logger(x, percent_last):
    percent_now = round((x / (x_size / 100)), 0)
    if percent_now > percent_last:
        print(str(percent_now) + '%', x, y)
        percent_last = percent_now
        return percent_last


def calc_color_up(prev_color):
    new_color = (prev_color[0] + 1, prev_color[1] + 1, prev_color[2] + 1)
    return new_color


def calc_color_down(prev_color):
    new_color = (prev_color[0] - 1, prev_color[1] - 1, prev_color[2] - 1)
    return new_color


def noise():
    percent_last = 0
    for x in range(0, x_size):
        for y in range(0, y_size):
            draw.point((x, y), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
            percent_last = percent_logger(x, percent_last)


def gradient():
    color = (0, 0, 0)
    direction = 1
    percent_last = 0
    for x in range(0, x_size):
        for y in range(0, y_size):
            # color changer direction changer
            if color[0] == 0 and direction == 0:
                direction = 1
            elif color[0] == 255 and direction == 1:
                direction = 0

            if direction == 1:
                color = calc_color_up(color)
            elif direction == 0:
                color = calc_color_down(color)

            draw.point((x, y), fill=color)
            percent_last = percent_logger(x, percent_last)


def image_preparer(content_type):


    if content_type == 1:
        noise()
    elif content_type == 2:
        gradient()



for content in (0, 1, 2):
    file = Image.new('RGB', (x_size, y_size))
    draw = ImageDraw.Draw(file)
    start = datetime.now()
    print(start)
    image_preparer(content)
    file.save(filename + str(content) + '.jpg', "JPEG")
    print(datetime.now())
    print(datetime.now() - start)
