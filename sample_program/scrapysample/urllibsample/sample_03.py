# ----- Webページをダウンロード -----
import urllib.request

url_page = 'http://www.baidu.com'

# url: ダウンロードソースの URL
urllib.request.urlretrieve(url_page, 'baidu.html')

# ----- 画像をダウンロード -----
url_img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTW9ZguUoPqT2' \
          '5SJAYhg1_kNCSpwLJI21oiPg&usqp=CAU'

urllib.request.urlretrieve(url=url_img, filename='nagasawamasami.jpg')

# ----- ビデオをダウンロード -----
url_video = 'https://vd2.bdstatic.com/mda-ndq3bk6h9pqm4sz1/cae_h264_delogo/16' \
            '50853796261465611/mda-ndq3bk6h9pqm4sz1.mp4?v_from_s=hkapp-haokan' \
            '-nanjing&auth_key=1650896466-0-0-88db16a151974192a698780d5bf35f2' \
            '6&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=3066784282&' \
            'vid=8989194195785322679&abtest=100815_2-101454_1-101830_1-17451_' \
            '2-3000222_2&klogid=3066784282'

urllib.request.urlretrieve(url_video, 'v.mp4')
