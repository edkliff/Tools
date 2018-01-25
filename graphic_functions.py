from random import randint


GRAY_DEVIATION = 0.001
COLOR_DEVIATION = 0.1


def percent_logger(x, x_size, y, percent_last):
    # percent_now = round((x / (x_size / 100)), 0)
    # if percent_now > percent_last:
    #     print(str(percent_now) + '%', x, y)
    #     percent_last = percent_now
    # return percent_last
    pass

def calc_color_up(prev_color):
    new_color = (prev_color[0] + GRAY_DEVIATION, prev_color[1] + GRAY_DEVIATION, prev_color[2] + GRAY_DEVIATION)
    return new_color


def calc_color_down(prev_color):
    new_color = (prev_color[0] - GRAY_DEVIATION, prev_color[1] - GRAY_DEVIATION, prev_color[2] - GRAY_DEVIATION)
    return new_color


def calc_color_red(prev_color):
    # new_color = ()
    if prev_color[2] > 0:
        new_color = (prev_color[0] + COLOR_DEVIATION, prev_color[1], prev_color[2]-COLOR_DEVIATION)
    else:
        new_color = (prev_color[0] + COLOR_DEVIATION, prev_color[1], prev_color[2])
    return new_color


def calc_color_green(prev_color):
    # new_color = ()
    if prev_color[0] > 0:
        new_color = (prev_color[0] - COLOR_DEVIATION, prev_color[1] + COLOR_DEVIATION, prev_color[2])
    else:
        new_color = (prev_color[0], prev_color[1] + COLOR_DEVIATION, prev_color[2])
    return new_color


def calc_color_blue(prev_color):
    # new_color = ()
    if prev_color[1] > 0:
        new_color = (prev_color[0], prev_color[1] - COLOR_DEVIATION, prev_color[2] + COLOR_DEVIATION)
    else:
        new_color = (prev_color[0], prev_color[1], prev_color[2] + COLOR_DEVIATION)
    return new_color


def noise(x_size, y_size, draw):
    percent_last = 0
    for x in range(0, x_size):
        for y in range(0, y_size):
            draw.point((x, y), fill=(randint(0, 255), randint(0, 255), randint(0, 255)))
            percent_last = percent_logger(x, x_size, y, percent_last)


def stripes(x_size, y_size, draw):
    color = (0, 0, 0)
    direction = 1
    percent_last = 0
    for x in range(0, x_size):
        for y in range(0, y_size):
            # color changer direction changer
            color_summ = color[0] + color[1] + color[2]
            if color[0] < 0 and direction == 0:
                direction = 1
            elif color[0] > 255 and direction == 1:
                direction = 0

            if direction == 1:
                color = calc_color_up(color)
            elif direction == 0:
                color = calc_color_down(color)

            draw.point((x, y), fill=(int(round(color[0], 0)), int(round(color[1], 0)), int(round(color[2], 0))))
            percent_last = percent_logger(x, x_size, y, percent_last)


def colorized(x_size, y_size, draw):
    color = (0, 0, 0)
    direction = 1
    percent_last = 0
    for x in range(0, x_size):
        if color[0] < 0 and direction == 3:
            direction = 1
        elif color[0] > 255 and direction == 1:
            direction = 2
        elif color[1] > 255 and direction == 2:
            direction = 3
        elif color[2] > 255 and direction == 3:
            direction = 1

        if direction == 1:
            color = calc_color_red(color)
        elif direction == 2:
            color = calc_color_green(color)
        elif direction == 3:
            color = calc_color_blue(color)

        for y in range(0, y_size):
            draw.point((x, y), fill=(int(round(color[0], 0)), int(round(color[1], 0)), int(round(color[2], 0))))
            percent_last = percent_logger(x, x_size, y, percent_last)


def image_preparer(content_type, x_size, y_size, draw):

    if content_type == 1:
        noise(x_size, y_size, draw)
    elif content_type == 2:
        stripes(x_size, y_size, draw)
    elif content_type == 3:
        colorized(x_size, y_size, draw)