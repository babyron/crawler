




"""
	新建文件夹
"""
from pathlib import Path


p = Path("J:\\------102-231-231=")
if not p.exists():
	try:
		p.mkdir()
	except FileNotFoundError:
		print("文件路劲不合法,请输入合法路径")




