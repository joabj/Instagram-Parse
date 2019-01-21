import json
import requests
from sys import argv
from pprint import pprint

response = open("joabjack.json", 'r')
data = json.load(response)

#target = open("Instagram.txt", 'w')

x = 0;

while x < 20:
	
	Earl = (data[x]['display_url'])
	print str(Earl)
	print "\r"
	TimeStamp = data[x]['taken_at_timestamp']
	print str(TimeStamp)
	print "\r"
	Height = data[x]['dimensions']['height']
	print int(Height)
	print "\r"	
	Width = data[x]['dimensions']['width']
	print int(Width)
	print "\r"	
	Caption = data[x]['edge_media_to_caption']['edges']
	#['node'][u'#text']
	print str(Caption)
	print "\r"
	print "-----------------------------------------------------------------------------------------------"
	x = x + 1
	
	
#target.close()

#pprint(data)
#For printing the taxonomy
