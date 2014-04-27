from html.parser import HTMLParser
import urllib.request
import re
import threading
from queue import Queue

def getHtml(url):
    page=urllib.request.urlopen(url)
    html = page.read().decode("utf-8")
    return html

class MyHTMLParser(HTMLParser):
	# x = 0
	# reg = r'.*(\.*?.jpg)'
	# imgre=re.compile(reg)
	def __init__(self, queue):
		HTMLParser.__init__(self)
		self.queue = queue
	def handle_starttag(self, tag, attrs):
		for name,value in attrs:
			# print(name," ",value)
			if(tag == "img"):
				for name, value in attrs:
					if(name == "src" and value[0] == 'h'):
					# urllib.request.urlretrieve(value,'D:\photos\%s.jpg' %self.x)
					# self.x += 1
				# print(value)
						self.queue.put(value)				

class PicUrlThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, g_name, html, queue):
		self.html = html
		self.queue = queue
		threading.Thread.__init__(self, name = g_name)
	def run(self):
		img_parser = MyHTMLParser(self.queue)
		img_parser.feed(self.html)
		img_parser.close

class PicReqThread(threading.Thread):
	"""docstring for MyThread"""
	def __init__(self, r_name, queue):
		threading.Thread.__init__(self,name = r_name)
		self.queue = queue
	def run(self):
		while not self.queue.empty():
			global x
			con.acquire()
			x += 1
			tmp = x
			con.release()
			# urllib.request.urlretrieve(self.queue.get(),'D:\photos\%s.jpg' %tmp)
			print(self.queue.get())
		
# parser = MyHTMLParser()
# while 1:
# 	cra_url = input("请输入要爬取图片的链接: ")
# 	try:
# 		html = getHtml(cra_url)
# 		break
# 	except ValueError:
# 		cra_url = input("请输入正确格式链接: ")

# parser.feed(html)
# parser.close()

con = threading.Condition()
x = 0
q = Queue()
# q.put("123")
# q.put("456")
html = getHtml("http://www.douban.com/photos/album/63958373/")
img_parser = MyHTMLParser(q)
img_parser.feed(html)
# pic = PicUrlThread("ask", html, q)
# pic.start()
# while not q.empty():
# 	print(q.get())
# for i in range(7):
# 	PicReqThread("req"+str(i), q).start()
PicReqThread("req", q).start()