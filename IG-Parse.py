import json
import requests
from sys import argv
from pprint import pprint

response = open("joabjack.json", 'r')
data = json.load(response)

#target = open("Instagram.txt", 'w')

x = 0;

while x < 20:
	print(data[x]['display_url'])
	print "\r"
	TimeStamp = data[x]['taken_at_timestamp']
	print str(TimeStamp)
	print "\r"
#	print(data[x]['dimensions'] ['height']: 1119, 
#            "width": 1080
	Caption = data[x]['edge_media_to_caption']['edges']
	#['node'][u'#text']
	print str(Caption)
	print "\r"
	x = x + 1
	
	
#target.close()

#pprint(data)
#For printing the taxonomy


#Docs
#https://learnpythonthehardway.org/book/ex16.html
#https://docs.python.org/3/tutorial/introduction.html#lists
#http://stackoverflow.com/questions/37771482/typeerror-list-indices-must-be-integers-not-unicode-telepot-retrieve-name
#http://stackoverflow.com/questions/11298767/decoding-json-to-give-me-a-certain-variable-in-python
#https://www.safaribooksonline.com/library/view/learning-geospatial-analysis/9781783281138/ch04s04.html
#http://stackoverflow.com/questions/11126902/decoding-json-string-in-python
#http://www.pythonforbeginners.com/requests/using-requests-in-python
#https://docs.python.org/3/library/json.html
#http://www.last.fm/api/show/user.getRecentTracks
#http://stackoverflow.com/questions/26895371/nameerror-name-requests-is-not-defined
#http://stackoverflow.com/questions/32040541/strange-python-issue-unicode-object-has-no-attribute-read
#https://www.safaribooksonline.com/library/view/javascript-json-cookbook/9781785286902/ch01s07.html#ch01lvl2sec33//
#https://linuxconfig.org/how-to-parse-data-from-json-into-python  --unknown variable 
#https://docs.python-guide.org/scenarios/json/
