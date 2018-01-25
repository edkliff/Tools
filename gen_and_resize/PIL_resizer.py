from PIL import Image
from datetime import datetime
from subprocess import call
from math import ceil
import xlwt

MED = 30

size = (1000, 1000)
PIL_times = []
IM_times = []

i = 2

for z in range(10000, 21000, 1000):
    res_times = []
    time = datetime.now()
    summ = time - time
    for c in range(1, MED):
        timestart = datetime.now()
        file = Image.open('timers-{}-{}.jpg'.format(str(i), str(z)))
        file.thumbnail(size)
        file.save('{}-{}-PIL.jpg'.format(str(i), str(z)), 'JPEG')
        timefinish = datetime.now()
        delta = timefinish - timestart
        res_times.append(delta)
        # print('PIL', i, z)
    for t in res_times:
        summ = summ + t
    median = summ / len(res_times)
    print(median)
    PIL_times.append(median)
print(PIL_times)


for z in range(10000, 21000, 1000):
    res_times = []
    time = datetime.now()
    summ = time - time
    for c in range(1, MED):
        timestart = datetime.now()
        call('convert "timers-{}-{}.jpg" -resize {}x{} "{}-{}-IM.jpg"'.format(str(i), str(z), size[0], size[1],
                                                                              str(i), str(z)), shell=True)
        timefinish = datetime.now()
        delta = timefinish - timestart
        res_times.append(delta)
        # print('IM', i, z)
    for t in res_times:
        summ = summ + t
    median = summ / len(res_times)
    print(median)
    IM_times.append(median)
print(PIL_times)


for t in range(0, len(PIL_times)):
    delta_IM_PIL = IM_times[t] - PIL_times[t]
    PIL_seconds = float(str(PIL_times[t]).split(':')[-1])
    IM_seconds = float(str(IM_times[t]).split(':')[-1])
    pic_num = t + 1
    resolution = pic_num * 1000
    print(resolution, PIL_seconds, IM_seconds)
