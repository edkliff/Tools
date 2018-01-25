import argparse
from PIL import Image, ImageDraw
from random import randint
from datetime import datetime
from graphic_functions import image_preparer

FILE = 'timers'
TYPE = 0
XSIZE = 1000
YSIZE = 500
CONTENT_NAMES_LIST = {
    0: 'Black',
    1: 'Noise',
    2: 'Gradient Stripes',
    3: 'Color Gradient'
}


parser = argparse.ArgumentParser(description='Picture generation')
parser.add_argument('--dest', action='store', type=str, default=FILE,
                    help='output filename, string')
parser.add_argument('--type', action='store', type=int, default=TYPE,
                    help="""type of file content:
                    {}""".format(CONTENT_NAMES_LIST))
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
start = datetime.now()

image_preparer(content, x_size, y_size, draw)
file.save('{}-{}-{}.jpg'.format(filename, str(content), x_size), "JPEG")

iteration_time = (datetime.now() - start).seconds
print(iteration_time, str(CONTENT_NAMES_LIST[content]), x_size)
