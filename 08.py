# This should solve integrity.html


from functools import reduce
import bz2
import re
import urllib.request

def main():

	urlbase = 'http://www.pythonchallenge.com/pc/def/integrity.html'

	try:
		with urllib.request.urlopen(urlbase) as f:
			urltext = f.read().decode('utf-8')
	except urllib.error.URLError as e:
		print(e.reason)

	
	print(urltext)

	pattern = re.compile("<!--\n(.*?)\n-->", re.S)
	text = pattern.findall(urltext)[-1]

	un, pw = map(lambda a: a[5:-1], text.split('\n'))

	# text is extracted from html comments
	# but does not convert to byte object...

	un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
	pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

	print(bz2.decompress(un).decode('utf-8'))
	print(bz2.decompress(pw).decode('utf-8'))

if __name__ == '__main__':
	main()