import requests
from bs4 import BeautifulSoup
from lxml import etree
from celebrity_beauty import Mysql

items = Mysql.get_star_url()
headers = {
    'Host':'www.yue365.com',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'
}
for item in items:
    url = item.get('star_url')
    r = requests.get(url,headers=headers)
    r.encoding = 'utf-8'
    response = r.text
    parser = etree.HTMLParser(encoding='utf-8')
    response2 = etree.HTML(response, parser=parser)
    star_img = response2.xpath('//div[@class="mx_tu f_l"]/img/@src')
    try:
        Mysql.insert_img(star_img, url)
    except Exception as e:
        # 打印错误日志
        print(e)