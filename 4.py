# This should solve linkedlist.php

import functools
import re
import urllib.request

def main():

	urlbase = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

	def nothing(n):
		return '?nothing=' + str(n)

	try:
		with urllib.request.urlopen(urlbase) as f:
			urltext = f.read().decode('utf-8')
	except urllib.error.URLError as e:
		print(e.reason)
	
	pattern = re.compile("<!--(.*?)-->", re.S)
	text = pattern.findall(urltext)[-1]

	print(text)

	# start index as hinted by the embedded hyperlink
	no_index = 12345
	# index just before the 'Divide by 2' - does not work from this point
	no_index = 3875
	# index exactly at the 'Divide by 2' - works from here???
	no_index = 16044

	for i in range(0,400):
		try:
			with urllib.request.urlopen(urlbase + nothing(no_index)) as f:
				urltext = f.read().decode('utf-8')
				no_search = re.search("and the next nothing is ([0-9]+)",urltext)
				if no_search == None:
					if no_index == 16044:
						no_index //= 2
						continue
						
					else:
						print(no_index)
						print(urltext)
						break
				else:
					no_index = no_search.group(1)
		except urllib.error.URLError as e:
			print(e.reason)
			exit(1)

if __name__ == '__main__':
	main()