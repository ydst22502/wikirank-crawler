import re
import urllib
import urllib2
import json

page = 2
base_url = 'http://wikirank.di.unimi.it/Q/?filter%5Btext%5D=Harmonic+centrality&filter%…e%5D=harmonic&view=list&pageSize=100&type=harmonic&score=false&pageIndex='
page_url = str(page)
url = base_url + page_url

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {}
headers = {'User-Agent' : user_agent}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
encodedJson = response.read()
decodedJson = json.loads(encodedJson)

ls = decodedJson['items']
for i in len(ls):
	print re.findall('.*?>(.*?)<', ls[i]['harmonic'])[0]
