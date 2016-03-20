import nltk
import re
from urllib import *
from bs4 import BeautifulSoup

import englishPlumb

url = "https://simple.wikipedia.org/wiki/United_States"
html = request.urlopen(url).read().decode('utf8')
raw = BeautifulSoup(html, "html.parser").get_text()
raw = raw.replace(u'\xa0', u' ')

sents = nltk.sent_tokenize(raw)

tokens = nltk.wordpunct_tokenize(raw)
text = nltk.Text(tokens)

fdist1 = nltk.FreqDist(text)
commonWord = [w for w,freq in fdist1.most_common(100) if w.isalpha() and w not in englishPlumb.englishPlumb] 

