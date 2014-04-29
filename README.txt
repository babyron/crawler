crawler
=======
实现思路:
	输入指令后，对指令进行解析，对指令参数做简单的校验，然后执行，其中最后的一项参数必须是url

指令实例： -n 10 -o D:\photos -l 20 http://www.22mm.cc

目录结构
--cc_crawler
 |--pics/	
 |--test/
 |    |-value_test.py
 |--crawler.py
 |--help.py
 |--READ.txt
 |--reg.txt

pics是默认的图片存放目录
test目录下的value_test.py有类Test里面包含三个静态方法，负责对指令参数校验
help.py处理帮助信息
reg.txt是图片名称过滤配置，每行代表一个正则表达式，图片名称符合任一表达式，便会被下载。#开头表示注释

crawler.py
----------
全局变量：
==========
save_path		图片保存目录，默认 工作目录/pics/
thread_num		线程的数目，默认为10
img_num			下载图片数目，默认-1，没有限制
img_list		保存下载图片链接
con				锁，实现img_list同步
reg_list		Pattern列表，实现对图片名称的过滤

类
==========
MyHTMLParser	继承自html.parser.HTMLParser
	类变量
	img_list	保存解析出的图片链接
	img_num		保存要下载的图片数目
	count		保存已经下载的图片数目

	类方法
	handle_starttag	覆盖父类方法，获取所有<img src="(http_url)" />括号部分的值，根据正则表达式对图片名称过滤，保存到img_list中

FetchPicThread	继承自threading.Thread
	类变量
	save_path	保存图片的路径

	类方法
	run			覆盖父类方法，首先获取全局变量con的锁，取出img_list对象的头部图片链接，释放锁，请求保存图片，图片命名方式为：线程名+tmp+图片原名（保证唯一）

模块
==========
get_img_name	给出图片url，获取图片名称
get_html		根据url请求html网页
get_host		获取url http://域名 部分
set_param		设置命令的参数（线程数，请求图片数目，保存目录，抓图地址）
parse_instru	解析指令，调用set_param
set_filter_reg	根据reg.txt中的表达式，把需要下载的图片链接匹配Patten对象保存在reg_list中
filter 			判断图片是否需要过滤
get_img_urls	新建MyHTMLParser对象，请求解析网页，过滤图片，最终把图片相对地址转化为绝对地址





