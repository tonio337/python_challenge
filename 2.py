# This should solve ocr.html

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
	print(set(text))


if __name__ == '__main__':
	main()