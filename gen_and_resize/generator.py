import xlwt
from datetime import datetime
from PIL import Image, ImageDraw
from graphic_functions import image_preparer

FILE = 'timers'
TYPE = 1
XSIZE = 1000
YSIZE = 1000
CONTENT_NAMES_LIST = {
    0: 'Black',
    1: 'Noise',
    2: 'Gradient Stripes',
    3: 'Color Gradient'
}

wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet', cell_overwrite_ok=True)


filename = FILE
content = 0
x_size = XSIZE
y_size = YSIZE

fullstart = datetime.now()



generation_types = (2, 3)

for scale in range(10, 21):
    x_size = XSIZE * scale
    y_size = YSIZE * scale
    ws.write(0, scale, scale)
    for content in generation_types:
        ws.write(content + 1, 0, content)
        print(CONTENT_NAMES_LIST[content], '№{}, resolution - {}'.format(scale, x_size))
        file = Image.new('RGB', (x_size, y_size))
        draw = ImageDraw.Draw(file)
        start = datetime.now()
        # print(start)
        image_preparer(content, x_size, y_size, draw)
        file.save('{}-{}-{}.jpg'.format(filename, str(content), x_size), "JPEG")
        # print(datetime.now())
        iteration_time = (datetime.now() - start).seconds
        print('{} seconds'.format(iteration_time))
        ws.write(content+1, scale, iteration_time)


print('Execution Time {}'.format(str(datetime.now() - fullstart)))
wb.save('times.xls')