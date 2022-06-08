import requests
import os
import re
from threading import Thread
import cv2
import numpy as np

def get_images_from_baidu(keyword, page_num, save_dir):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36'}
    url = 'https://image.baidu.com/search/acjson?'
    n = 0
    for pn in range(0, 30 * page_num, 30):
        param = {'tn': 'resultjson_com',
                 'ipn': 'rj',
                 'ct': 201326592,
                 'is': '',
                 'fp': 'result',
                 'queryWord': keyword,
                 'cl': 2,
                 'lm': -1,
                 'ie': 'utf-8',
                 'oe': 'utf-8',
                 'adpicid': '',
                 'st': -1,
                 'z': '',
                 'ic': '',
                 'hd': '',
                 'latest': '',
                 'copyright': '',
                 'word': keyword,
                 's': '',
                 'se': '',
                 'tab': '',
                 'width': '',
                 'height': '',
                 'face': 0,
                 'istype': 2,
                 'qc': '',
                 'nc': '1',
                 'fr': '',
                 'expermode': '',
                 'force': '',
                 'cg': '',    # 这个参数没公开，但是不可少
                 'pn': pn,    # 显示：30-60-90
                 'rn': '30',  # 每页显示 30 条
                 'gsm': '1e',
                 '1618827096642': ''
                 }
        request = requests.get(url=url, headers=header, params=param)
        if request.status_code == 200:
            print('Request success.')
        request.encoding = 'utf-8'

        html = request.text
        image_url_list = re.findall('"thumbURL":"(.*?)",', html, re.S)
        print(image_url_list)

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        for image_url in image_url_list:
            image_data = requests.get(url=image_url, headers=header).content
            with open(os.path.join(save_dir, f'{n:06d}.jpg'), 'wb') as fp:
                fp.write(image_data)
            n = n + 1


if __name__ == '__main__':
    '''
    keyword1 = '猫'
    save_dir1 = 'cat'
    page_num1 = 10
    keyword2 = '狗'
    save_dir2 = 'dog'
    page_num2 = 10

    t1 = Thread(target=get_images_from_baidu, args=(keyword1, page_num1, save_dir1))
    t1.start()
    t2 = Thread(target=get_images_from_baidu, args=(keyword2, page_num2, save_dir2))
    t2.start()
    t1.join()
    t2.join()
    print('Get cat images finished.')
    print('Get dog images finished.')

    '''
    '''
    image_path='cat/000000.jpg'
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    h, w, c = img.shape
    shrink = cv2.resize(img, (0, 0), fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    enlarge = cv2.resize(img, (0, 0), fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    dst1 = cv2.flip(img, 0)
    dst2 = cv2.flip(img, 1)
    dst3 = cv2.flip(img, -1)
    cv2.imshow('origin', img)
    cv2.imshow('shrink', shrink)
    cv2.imshow('enlarge', enlarge)
    cv2.imshow('up to down', dst1)
    cv2.imshow('right to left', dst2)
    cv2.imshow('point to point', dst3)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

    path_cat = r'E:/TEST/cat'
    dirs = os.listdir(path_cat)
    for i in range(len(dirs)-1):
        path = os.path.join(path_cat, dirs[i])
        img = cv2.imread(path, 1)
        Str = "cat-%d.jpg" % i
        cv2.imwrite("E:/TEST/cat/rename" + "/" + Str, img)
    path_dog = r'E:/TEST/dog'
    dirs = os.listdir(path_dog)
    for i in range(len(dirs)-1):
        path = os.path.join(path_dog, dirs[i])
        img = cv2.imread(path, 1)
        Str = "dog-%d.jpg" % i
        cv2.imwrite("E:/TEST/dog/rename" + "/" + Str, img)


