import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import time
import nltk
import random

def birth(mon = 'March', day = '1'):
	base_url = 'http://www.famousbirthdays.com/'
	url = base_url + mon.lower() + day + '.html'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	values = {}
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	data = urllib.urlencode(values)
	request = urllib2.Request(url, headers = hdr)
	try:
		response = urllib2.urlopen(request)
	except urllib2.URLError, e:
		print e.code
		return 'URLError'
	html = response.read()

	rePattern = '<a class="celeb".*?<span class="title">(.*?), (.*?)</span>'
	infos = re.findall(rePattern, html, re.S)

	if len(infos) < 1:
		return ''

	if len(infos[0][0]) > 20:
		return ''
	try:
		int(infos[0][1])
	except:
		return ''

	question_style = random.randint(1, 3)
	if question_style == 1:
		return 'Q: When was ' + infos[0][0] + ' born?\n' + 'A: ' + mon + ' ' + day + ', ' +str(2016 - int(infos[0][1])) + '\n'
	if question_style == 2:
		return 'Q: When is ' + infos[0][0] + '\'s birthday?\n' + 'A: ' + mon + ' ' + day + ', ' +str(2016 - int(infos[0][1])) + '\n'
	if question_style == 3:
		return 'Q: What is the date of ' + infos[0][0] + '\'s birthday?\n' + 'A: ' + mon + ' ' + day + ', ' +str(2016 - int(infos[0][1])) + '\n'


def digit2date(m = 1):
	mon_table = ['NONE', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
	return mon_table[m]

###########main###############

fp = open('celeb_birth_qa2.dat', 'w')

for m in range(1, 13):
	for d in range(1, 32):
		qaStr = birth(digit2date(m), str(d))
		if qaStr != '':
			print m, d
			fp.write(qaStr)
fp.close()

























