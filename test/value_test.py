from pathlib import Path
import re

class Test():
	"""
		对指令参数做简单的校验,增加容错能力
	"""
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
		else:
			return True

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
		"""
			url路径校验
		"""
		reg = re.compile(
        r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' 
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
		reg_pat = re.compile(reg)
		return reg_pat.match(url)
