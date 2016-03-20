import urllib
import urllib2
import re
from bs4 import BeautifulSoup

keyword = 'English language'
base_url = 'https://en.wikipedia.org/wiki/'
url = base_url + keyword
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {}
headers = {'User-Agent' : user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
the_page = response.read()
#unicodePage = the_page.decode('utf-8')

p1 = re.findall('<div.*?id="mw-content-text".*?<p>(.*?)</p>.*?', the_page, re.S)
raw_p1 = BeautifulSoup(p1[0], "lxml").get_text()
#print raw_p1

#remove [1][13]..
pattern1 = re.compile(r'\[\d+\]')
p1_without_bracket = pattern1.sub('', raw_p1)

#remove ()...
pattern2 = re.compile(r'\s\(.+?\)')
p1_without_parentheses = pattern2.sub('', p1_without_bracket)

print p1_without_parentheses