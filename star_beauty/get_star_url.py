import requests
from bs4 import BeautifulSoup
from lxml import etree
from celebrity_beauty import Mysql
headers = {
    'Host':'www.yue365.com',
    'Referer':'http://www.yue365.com/mingxing/zimu/z.shtml',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36'
}
def get_star(x):
    x = chr(x)
    url = 'http://www.yue365.com/mingxing/zimu/' + x + '.shtml'
    r = requests.get(url, headers=headers)
    r.encoding = 'utf-8'
    response = r.text
    parser = etree.HTMLParser(encoding='utf-8')
    response2 = etree.HTML(response,parser=parser)
    star_count = response2.xpath('//p/a/text() ')
    for i in range(10):
        try:
            star_name = response2.xpath('//p/a/text() ')[i]
            star_url = 'http://www.yue365.com' + response2.xpath('//p/a/@href')[i]
        except:
            break;
        try:
            Mysql.insert_stars(star_name, star_url)
        except Exception as e:
            # 打印错误日志
            print(e)

    try:
        soup = BeautifulSoup(r.content.decode(), 'html.parser')

        body = soup.body
        stars_as = body.find_all('a', attrs={'class': 'show'})
        stars_bs = body.find_all('a', attrs={'class': 'dis-112'})
        for star in stars_as:
            star_url = 'http://www.yue365.com' + star['href']
            star_name = star.string
            try:
                Mysql.insert_stars(star_name,star_url)
            except Exception as e:
                # 打印错误日志
                print(e)
        for star in stars_bs:
            star_url = 'http://www.yue365.com' + star['href']
            star_name = star.string
            try:
                Mysql.insert_stars(star_name,star_url)
            except Exception as e:
                # 打印错误日志
                print(e)
    except:
        pass

for x in range(97,123):
    get_star(x)
