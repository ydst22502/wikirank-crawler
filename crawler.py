import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import time
import nltk

#return the paragraph 1 of the Wiki article of keyword
def wiki(keyword = 'Wiki'):
	base_url = 'https://en.wikipedia.org/wiki/'
	url = base_url + keyword
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	values = {}
	#headers = {'User-Agent' : user_agent}
	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
	data = urllib.urlencode(values)
	request = urllib2.Request(url, data, hdr)
	try:
		response = urllib2.urlopen(request)
	except urllib2.URLError, e:
		print e.code
		return 'URLError'
	the_page = response.read()
	the_page = the_page[:50000]
	#unicodePage = the_page.decode('utf-8')

	rePattern = '<div.*?id="mw-content-text".*?<table class="infobox.*?</table>.*?<p>(.*?)</p>.*?'+\
	'|'+'<div.*?id="mw-content-text".*?<p>(.*?<b>'+keyword+'</b>.*?)</p>.*?'

	p1 = re.findall(rePattern, the_page, re.S|re.I)
	if len(p1) == 0:
		return 'NONE MATCH'
	raw_p1 = BeautifulSoup(p1[0][0] + p1[0][1], "lxml").get_text()
	#print raw_p1

	#remove []..
	pattern1 = re.compile(r'\[.+?\]')
	p1_without_bracket = pattern1.sub('', raw_p1)

	#remove ()...
	pattern2 = re.compile(r'\s\(.+?\)')
	p1_without_parentheses = pattern2.sub('', p1_without_bracket)

	#remove )...
	p1_without_parentheses = p1_without_parentheses.replace(')', '')

	#remove / / ...
	pattern3 = re.compile(r'\W.*?\/.+?\/')
	p1_without_slash = pattern3.sub('', p1_without_parentheses)

	return p1_without_slash

def isWho(paragraph):
	pps = ['he', 'his', 'him', 'she', 'her']
	tokens = nltk.word_tokenize(paragraph)
	paragraph_token_set = set(tokens)
	for pp in pps:
		if pp in paragraph_token_set:
			return True
	return False

def question_generation_who_what(paragraph, keyword):
	sent_tokens = nltk.sent_tokenize(paragraph)
	if isWho(paragraph):
		print 'Q: Who is ' + keyword + '?'
	else:
		print 'Q: What is ' + keyword + '?'
	print 'A: ' + sent_tokens[0]
	print
	

fp = open('keywords_50000.dat', 'r')
number_of_kewords = int(fp.readline()[:-1])
keywords = []
for n in range(number_of_kewords):
	keywords.append(fp.readline()[:-1])

for n in range(968, 999):
	print n, keywords[n]
	print
	paragraph1 = wiki(keywords[n])
	question_generation_who_what(paragraph1, keywords[n])
	print paragraph1
	print
	print '**********************************************'
	print
	time.sleep(2)

#Debug
#print wiki('Justin Bieber')

fp.close()



















