
import re

m  = re.compile(r".*?.jpg$")
while 1:
	a = input("str")
	b = m.match(a)
	if b:
		print(b.group())
	else:
		print("hehe")
