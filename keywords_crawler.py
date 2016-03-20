# -*- coding: utf-8 -*-
import re
import urllib
import urllib2
import json

total_page = 970

fp = open('keywords.dat', 'w')
fp.write(str(total_page*5000) + '\n')

for page in range(total_page):

	print 'Crawling page:', page, '/', total_page;

	base_url = 'http://wikirank.di.unimi.it/Q/?filter%5Btext%5D=Harmonic+centrality&filter%…e%5D=harmonic&view=list&pageSize=5000&type=harmonic&score=false&pageIndex='
	page_url = str(page)
	url = base_url + page_url

	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	values = {}
	headers = {'User-Agent' : user_agent}
	data = urllib.urlencode(values)
	request = urllib2.Request(url, headers=headers)
	response = urllib2.urlopen(request)
	encodedJson = response.read()
	decodedJson = json.loads(encodedJson, strict=False)

	ls = decodedJson['items']
	tempStr = ''
	for i in range(len(ls)):
		tempStr += re.findall('.*?>(.*?)<', ls[i]['harmonic'])[0] +'\n'
		#fp.write(re.findall('.*?>(.*?)<', ls[i]['harmonic'])[0].encode('utf-8')+'\n')
	fp.write(tempStr.encode('utf-8'))

fp.close()