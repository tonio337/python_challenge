# This should solve ocr.html

import functools
import re
import urllib.request

def main():
	try:
		with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html') as f:
			urltext = f.read().decode('utf-8')
	except urllib.error.URLError as e:
		print(e.reason)
	
	pattern = re.compile("<!--\n(.*?)\n-->", re.S)
	text = pattern.findall(urltext)[-1]

	# Fix this line and we're pretty much done...
	# Look for characters in range ['a'..'z']
	rarechars = list(filter(lambda a: a >= 'a' and a <= 'z', text))

	print(functools.reduce(lambda a,b: a+b, rarechars))


if __name__ == '__main__':
	main()