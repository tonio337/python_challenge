# This should solve equality.html

import functools
import re
import urllib.request

def main():
	try:
		with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/equality.html') as f:
			urltext = f.read().decode('utf-8')
	except urllib.error.URLError as e:
		print(e.reason)
	
	pattern = re.compile("<!--\n(.*?)\n-->", re.S)
	text = pattern.findall(urltext)[-1]

	#print(text)

	# Fix this line and we're pretty much done...
	# Look for characters in range ['a'..'z']
	#rarechars = list(filter(lambda a: a >= 'a' and a <= 'z', text))

	#print(functools.reduce(lambda a,b: a+b, rarechars) + '.html')

	small = re.compile('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]')
	print(functools.reduce(lambda a,b: a+b,small.findall(text)))


if __name__ == '__main__':
	main()