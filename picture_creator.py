import argparse
from PIL import Image, ImageDraw
from random import randint

FILE = 'pic.jpg'
TYPE = 1
XSIZE = 10000
YSIZE = 5000

parser = argparse.ArgumentParser(description='Picture generation')
parser.add_argument('--dest', action='store', type=str, default=FILE,
                    help='output filename, string')
parser.add_argument('--type', action='store', type=int, default=TYPE,
                    help="""type of file content:
                    0 - Empty
                    1 - Noise""")
parser.add_argument('--xsize', action='store', type=int, default=XSIZE,
                    help='horizontal size of image')
parser.add_argument('--ysize', action='store', type=int, default=YSIZE,
                    help='vertical size of image')

arguments = parser.parse_args()
filename = arguments.dest
content = arguments.type
x_size = arguments.xsize
y_size = arguments.ysize

file = Image.new('RGB', (x_size, y_size))
draw = ImageDraw.Draw(file)


def draw_furball():
    pass


# Noise

if content == 1:
    for x in range(0, x_size):
        for y in range(0, y_size):
            draw.point((x, y), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
            if (x % 100 == 0) and (y % 100 == 0):
                print(x, y)

# Fur
elif content == 2:
    for x in range(0, x_size):
        for y in range(0, y_size):
            draw_furball()
            if (x % 100 == 0) and (y % 100 == 0):
                print(x, y)


file.save(filename, "JPEG")