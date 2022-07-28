import re
import urllib.request

urlbase = 'http://www.pythonchallenge.com/pc/def/'

def url_text(filename):
	try:
		with urllib.request.urlopen(urlbase + filename) as f:
			urltext = f.read().decode('utf-8')
	except urllib.error.URLError as e:
		print(e.reason)
	return urltext

def comments(text):
	pattern = xre.compile("<!--\n(.*?)\n-->", re.S)
	return pattern.findall(urltext)