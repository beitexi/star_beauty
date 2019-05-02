import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='sjq258369',
                             db='star',
                             port = 3306,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# 导入歌手名字，网址
def insert_stars(star_name, star_url):

    with connection.cursor() as cursor:
        sql = "INSERT INTO `star` (`STAR_NAME`, `STAR_URL`) VALUES (%s, %s)"
        cursor.execute(sql, (star_name, star_url))
    connection.commit()




# 获取所有明星的 网址
def get_star_info():
    with connection.cursor() as cursor:
        sql = "SELECT star_name,star_img FROM star"
        cursor.execute(sql)
        return cursor.fetchall()

# 获取
def get_star_url():
    with connection.cursor() as cursor:
        sql = "SELECT star_url FROM star"
        cursor.execute(sql)
        return cursor.fetchall()

# 导入歌手的图片地址
def insert_img(star_img,star_url):
    with connection.cursor() as cursor:
        sql = "UPDATE `star` SET star_img = %s WHERE star_url = %s"
        cursor.execute(sql, (star_img, star_url))
    connection.commit()

def insert_star_beauty(star_name,star_beauty):
    with connection.cursor() as cursor:
        sql = "UPDATE `star` SET star_beauty = %s WHERE star_name = %s"
        cursor.execute(sql, (star_beauty, star_name))
    connection.commit()