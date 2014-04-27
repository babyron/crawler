from help import *
import os
import sys
sys.path.append("..")
from cc_crewler.test.value_test import Test

def set_param(param, value):
	if param == "-n":
		if Test.num_test(value):
			global thread_num
			thread_num = value
			return False
		else:
			print("进程数目不合法")
	elif param == "-o":
		if Test.fifile_name_test(value):
			global save_path
			save_path = value
			return True
		else:
			print("文件路径不合法")
	elif param == "-l":
		if Test.num_test(value):
			global img_num
			img_num = value
			return True
		else:
			print("图片数目不合法")
	else:
		print("参数错误")
	return False


def parse_instru(params):
	if len(params) % 2 == 0:
		print("参数个数错误")
		return False
	for i in range(0, len(params) - 1, 2):
		# print("i = {0}".format(i))
		if(not set_param(params[i], params[i + 1])):
			return False
	if not Test.url_test(params[len(params) - 1]):
		print("链接格式错误")
		return False
	return True


def handle_instru(path, threads, num, url):
	print("")


save_path = os.getcwd() + "\\pics"
thread_num = 10
img_num = -1
url = None

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
			handle_instru(save_path, thread_num, img_num, url)


