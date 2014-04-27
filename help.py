help ='''\t[-h]\t获取帮助
\t[[-n int] [-o str] [-l int]]\t指令格式
\t-h\t查看程序运行帮助
\t-n\t指定进程数目
\t-o\t选择图片存储目录
\t-l\t选择爬取图片数目'''
legal_param = ['-h','-n','-o','-l']

def help_info():
	print(help)

# def legal_instru(instr):
# 	instr_params = instr.split(" ")
# 	if(len(instr_params)== 1 and instr_params[0] == "-h"):
# 		help_info()
# 	else:
# 		print('指令错误,输入-h查看帮助')
# 	print(len(instr_params))
# 	return instr_params
