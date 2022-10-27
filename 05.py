# This should solve peak.html

import pickle
import re
import urllib.request

def main():

	urlbase = 'http://www.pythonchallenge.com/pc/def/banner.p'

	try:
		with urllib.request.urlopen(urlbase) as f:
			my_pickle = pickle.load(f)
	except urllib.error.URLError as e:
		print(e.reason)
		exit(1)

	msg = map(reduce_line,my_pickle)

	for line in msg:
		print(line)

def reduce_line(line):
	acc = ""; [acc := acc + expand_tuple(x) for x in line]
	return acc

def expand_tuple(tup):
	return tup[0] * tup[1]

if __name__ == '__main__':
	main()