import requests
import json
import base64
import json
import requests
from celebrity_beauty import Mysql
import os
from os.path import join as pjoin
import time


img_dir = 'G:/reptilian/celebrity_beauty/img'


def get_img_base(file):
    with open(file,'rb') as fp:
        content = base64.b64encode(fp.read())
        return content


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


def beauty_test(img):

    token = '24.e688d1e9b6e5a58c5690cf6b8293a98c.2592000.1558185116.282335-16056062'
    requests_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    requests_url = requests_url + '?access_token=' + token
    headers = {
        'Content-Type': 'application/json'
    }
    params = {
        'image': get_img_base(img),
        'image_type': 'BASE64',
        'face_field': 'age,beauty,gender',
        'max_face_num': 3,
    }

    res = requests.post(requests_url, data=params, headers=headers)
    result = res.text
    json_result = json.loads(result)
    try:
        beauty = json_result['result']['face_list'][0]['beauty']
    except:
        beauty = 0
    return beauty

load_data(img_dir)
