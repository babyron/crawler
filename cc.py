
import re
import sys
import chardet
import urllib.request
import urllib.parse


def getHtml(url):
    page=urllib.request.urlopen(url)
    # print(sys.getfilesystemencoding())
    html = page.read().decode("utf-8")
    # html=page.read().decode("gbk").encode(sys.getfilesystemencoding())
    # print(html)
    return html

def get_host(url):
    url_domain = urllib.parse.urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=url_domain)
    return domain

def getImg(domain, html):
    reg= r'src="(.*?\.jpg)"'
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    x=0
    # print(imglist)
    for imgurl in imglist:
        print(imgurl+"\n")
        # urllib.request.urlretrieve(domain + imgurl,'D:\photos\%s.jpg' %x)
        # x+=1

http_url = input("输入要抓去图片的链接")  
images_html = getHtml(http_url)
domain = get_host(http_url);
getImg(domain, images_html)