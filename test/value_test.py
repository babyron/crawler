from pathlib import Path
import re

class Test():

	@staticmethod
	def file_name_test(file_path):
		"""
			新建目录
			验证目录名称格式是否正确
		"""
		p = Path(file_path)
		if not p.exists():
			try:
				p.mkdir()
				return True
			except:
				return False

	@staticmethod
	def num_test(thread_num):
		"""
			验证进程数目是否是数字
		"""
		for x in thread_num:
			if(not x.isdigit()):
				return False
		return True

	@staticmethod
	def url_test(url):
		reg = "http://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)?"
		reg_pat = re.comile(reg)
		return reg_pat.match(url)
