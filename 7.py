# This should solve channel.html

from functools import reduce
from PIL import Image
import re
import urllib.request
import zipfile

def main():

	urlbase = 'http://www.pythonchallenge.com/pc/def/channel.html'

	try:
		with urllib.request.urlopen(urlbase) as f:
			urltext = f.read().decode('utf-8')
	except urllib.error.URLError as e:
		print(e.reason)

	image = Image.open('oxygen.png')

	acc = []

	for w in range(0,image.width,7):
		acc.append(image.getpixel((w, image.height//2))[0])

	mapped = map(lambda a: chr(a), acc)
	print(reduce(lambda a,b: a+b, mapped))

	finalmsg = [105,110,116,101,103,114,105,116,121]

	finalmap = map(lambda a: chr(a), finalmsg)
	print(reduce(lambda a,b: a+b, finalmap))

if __name__ == '__main__':
	main()