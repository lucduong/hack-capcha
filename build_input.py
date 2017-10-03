import cv2
from PIL import Image, ImageChops
import os
import os.path
from os import listdir
from os.path import join, isfile, basename

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TMP_DATA_DIR = CURRENT_DIR + "/tmp/data"
DATA_DIR = CURRENT_DIR + "/data"


def explore_jpg(dir_path):
    file_list = []
    for file_name in listdir(dir_path):
        file_path = join(dir_path, file_name)
        if isfile(file_path) and 'jpg' in file_name:
            file_list.append(file_path)
    return file_list


def reduce_noise(absolute_path):
    file_name = basename(absolute_path)
    img = cv2.imread(absolute_path)
    dst = cv2.fastNlMeansDenoisingColored(img, None, 50, 50, 7, 21)
    tmp_file = TMP_DATA_DIR + "/" + file_name
    cv2.imwrite(tmp_file, dst)
    img = Image.open(tmp_file).convert('L')
    img = img.point(lambda x: 0 if x < 150 else 255, '1')
    img.save(DATA_DIR + "/" + file_name)


def reduce_noise_in(dir_path="rawdata"):
    print("reducing noise in " + dir_path)
    image_paths = explore_jpg(dir_path)
    print("There are " + len(image_paths) + " need to reduce noise")


# reduce_noise("/Users/luc/Downloads/raw/0004.jpg")
