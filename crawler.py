from help import *
import os
import sys
sys.path.append("..")
from cc_crawler.test.value_test import Test
from urllib import parse
from urllib import request
from html.parser import HTMLParser
import threading
import re

class   MyHTMLParser(HTMLParser):
	def __init__(self, img_num):
		HTMLParser.__init__(self)
		self.img_list = []
		self.img_num = img_num
		self.count = 0
	def handle_starttag(self, tag, attrs):
		if self.img_num == -1 or self.img_num > self.count and tag == "img":
			for name, value in attrs:
				if name == "src":
					img_name = get_img_name(value)
					if filter(img_name):
						self.img_list.append(value)
						self.count += 1
						break

class   FetchPicThread(threading.Thread):
	def __init__(self, r_name, save_path):
		threading.Thread.__init__(self,name = r_name)
		self.save_path = save_path
	def run(self):
		global img_list
		global con
		tmp = 1
		while 1:
			if  img_list:
				con.acquire()
				top = img_list.pop()
				con.release()
				img_name = get_img_name(top)
				request.urlretrieve(top,"{0}\{1}{2}{3}".format(self.save_path ,self.name ,tmp, img_name))
				tmp += 1
			else:
				break

"""
	获取url地址中图片名字
"""
def get_img_name(url):
	return os.path.basename(url)

"""
	获取html
"""
def get_html(url):
    page = request.urlopen(url)
    html = page.read().decode("utf-8")
    return html

"""
	获取url中http://domain部分
"""
def get_host(url):
    url_domain = parse.urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri = url_domain)
    return domain

"""
	设置指令执行需要的参数
"""
def set_param(param, value):
	"""
		对命令行的参数进行校验
		设置参数
	"""
	if param == "-n":
		if Test.num_test(value):
			global thread_num
			thread_num = int(value)
			return True
		else:
			print("进程数目不合法")
	elif param == "-o":
		if Test.file_name_test(value):
			global save_path
			save_path = value
			return True
		else:
			print("文件路径不合法")
	elif param == "-l":
		if Test.num_test(value):
			global img_num
			img_num = int(value)
			return True
		else:
			print("图片数目不合法")
	else:
		print("参数错误")
	return False

"""
	解析指令
	简单校验参数
"""
def parse_instru(params):
	if len(params) % 2 == 0:
		print("参数个数错误")
		return False
	for i in range(0, len(params) - 1, 2):
		if(not set_param(params[i], params[i + 1])):
			return False
	if not Test.url_test(params[len(params) - 1]):
		print("链接格式错误")
		return False
	return True

"""
	将path中的所有正则表达式
	编译成Pattern对象
	保存到reg_list中
	@param path 配置文件路径
"""
def set_filter_reg(path):
	return [re.compile(eval(line)) for line in open(path) if line[0] != "#"]

"""
	对图片名称进行过滤
"""
def filter(url):
	global reg_list
	for pat in reg_list:
		m = pat.match(url)
		if 	m:
			return True
	return False


"""
	解析网页
	获取网页中所有<img />标签的src属性值
	将值保存到parser的img_list中
	处理相对地址
	返回地址列表
	@param url 要解析的网页地址
	@param img_num 要下载的图片数目
"""
def get_img_urls(url, img_num):
	html = get_html(url)
	parser = MyHTMLParser(img_num)
	parser.feed(html)
	domain = get_host(url)
	for i in range(len(parser.img_list)):
		if parser.img_list[i][0 : 4] == 'http':
			pass
		else:
			parser.img_list[i] = domain + parser.img_list[i]
	return parser.img_list

if __name__ == '__main__':
	save_path = os.getcwd() + "\\pics"
	thread_num = 10
	img_num = -1
	con = threading.Condition()
	reg_list = set_filter_reg("reg.txt")

	while 1:
		instru = input("请输入指令:")
		params = instru.split()
		if len(params) == 1 and params[0] == "-h":
				help_info()
				continue
		else:
			if not parse_instru(params):
				help_info()
				continue
			else:
				img_list = get_img_urls(params[len(params) - 1], img_num)
				for i in range(thread_num):
					FetchPicThread("Thread{0}".format(i),save_path).start()
				break

