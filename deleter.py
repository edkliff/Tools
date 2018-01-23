import os
import datetime
from time import sleep
import argparse
from sys import stdout

"""
Small tool for removing old files in temp directories, 
"""


DIRECTORY = '/opt/round.me/upload/'
# count of days for files. All files in directory older then this count will be removed
MAX_DELTA = 1
# in minutes
PAUSE = 60


def lists():
    os.chdir(file_place)
    files_list = os.listdir(file_place)
    return files_list


def deletion(time, files_list):
    for file in files_list:
        if os.path.isfile(file_place + file):
            time_file = os.path.getmtime(file_place + file)
            time_file = datetime.datetime.fromtimestamp(time_file)
            delta = time - time_file
            if delta.days >= delta_days:
                print('Removing: {}'.format(file_place + file))
                os.remove(file_place + file)


parser = argparse.ArgumentParser(description='Simple deletion for old files')
parser.add_argument('--dest', action='store', type=str, default=DIRECTORY, help='directory for cleaning, string')
parser.add_argument('--days', action='store', type=int, default=MAX_DELTA,
                    help='count of days for files. All files in directory older then this count will be removed, int')
parser.add_argument('--paus', action='store', type=int, default=PAUSE,
                    help='how many minutes script wait before next deletion, int')
arguments = parser.parse_args()
file_place = arguments.dest
delta_days = int(arguments.days)
period = int(arguments.paus)

print(arguments)

if file_place[-1] != '/':
    file_place = file_place + '/'
    print(file_place)


while True:
    time_now = datetime.datetime.now()
    print(str(time_now))
    content = lists()
    deletion(time_now, content)
    stdout.flush()
    sleep(period * 60)
