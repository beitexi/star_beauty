import requests
import json
import base64
import requests
from hashlib import md5
from celebrity_beauty import Mysql
from requests import codes
import os
from os.path import join as pjoin
# from scipy import misc
img_dir = 'G:/reptilian/celebrity_beauty/img'

def load_data(img_dir):  # data_dir是lfw数据集路径
    for guy in os.listdir(img_dir):
        star_name = guy
        person_dir = pjoin(img_dir, guy)  # lfw中文件夹的路径
        # print()
        for i in os.listdir(person_dir):
            image_dir = img_dir + r'/' + star_name + r'/' + i
            star_beauty = beauty_test(image_dir)
            try:
                print(star_name,star_beauty)
                Mysql.insert_star_beauty(star_name, star_beauty)
            except Exception as e:
                # 打印错误日志
                print(e)





def save_image(item):
    img_path = 'img' + os.path.sep + item.get('star_name')
    print('succ2')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('star_img'))
        if codes.ok == resp.status_code:
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                print('succ3')
                with open(file_path, 'wb') as f:
                    f.write(resp.content)
                print('Downloaded image path is %s' % file_path)
                print('succ4')
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to Save Image，item %s' % item)


def save_img2():
    items = Mysql.get_star_info()
    for item in items:
        save_image(item)

# save_img2()
# load_data(img_dir)
items = Mysql.get_star_info()
for item in items:
    print(item)


