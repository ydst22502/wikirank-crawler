import urllib
import urllib2
import re
import time
import nltk
import en
import random
from nltk.tag import pos_tag
from bs4 import BeautifulSoup

fp = open('19th_history_qa.dat', 'w')

url = 'https://en.wikipedia.org/wiki/19th_century#Events'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

request = urllib2.Request(url, headers = hdr)
try:
	response = urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.code

html = response.read()

rePattern = '<li>.*?title="\d\d.*?">(.*?)</a>(.*?)</li>'
sentss = re.findall(rePattern, html, re.S)

for year, sents in sentss:
	sents = sents[1:] #remove :
	raw_sents = BeautifulSoup(sents, "lxml").get_text()
	tokenized_sents = nltk.sent_tokenize(raw_sents)
	for sent in tokenized_sents:
		#print 'Source: ', sent
		tokens = nltk.word_tokenize(sent)

		#tag pos
		tagged_sent = pos_tag(tokens)

		#tense transform
		for n, (word, pos) in enumerate(tagged_sent):
			if en.verb.infinitive(word) != '':
				tagged_sent[n] = (en.verb.infinitive(word), pos)


		#1st word upper or lower case 
		if tagged_sent[0][1] != 'NNP':
			tagged_sent[0] = (tagged_sent[0][0].lower(), tagged_sent[0][1])

		#have at least one verb
		#print tagged_sent
		
		if ('VBZ' in [pos for word, pos in tagged_sent])\
		or ('VBD' in [pos for word, pos in tagged_sent])\
		or ('VB' in [pos for word, pos in tagged_sent])\
		or ('VBG' in [pos for word, pos in tagged_sent])\
		or ('VBN' in [pos for word, pos in tagged_sent])\
		or ('VBP' in [pos for word, pos in tagged_sent]):
			q_style = random.randint(1,2)
			finalStr = ' '.join([word for word, pos in tagged_sent[:-1]]).encode('utf8')
			if q_style == 1:
				fp.write('Q: Which year did '+ finalStr + '?\n')
			if q_style == 2:
				fp.write('Q: When did '+ finalStr + '?\n')
			fp.write('A: In ' + year + '\n')
	print year
fp.close()

		