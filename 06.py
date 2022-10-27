# This should solve channel.html

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

	##print(urltext)

	my_zip = zipfile.ZipFile('./channel.zip')

	#print(my_zip.namelist())
	print(my_zip.read('readme.txt'))

	nothing = 90052
	acc = my_zip.comment.decode()

	for i in range(0,1000):
		contents = my_zip.read(str(nothing) + '.txt').decode()
		print(contents)
		nothing_search = re.search("Next nothing is ([0-9]+)",contents)
		if (nothing_search == None):
			print(acc)
			break
		else:
			nothing = nothing_search.group(1)
			acc += my_zip.getinfo(str(nothing) + '.txt').comment.decode()
			continue


if __name__ == '__main__':
	main()