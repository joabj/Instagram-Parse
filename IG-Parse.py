import json
import requests
from sys import argv
from pprint import pprint

response = open("joabjack.json", 'r')
data = json.load(response)

target = open("Instagram.txt", 'w')

x = 0;

while x < 20:

	
	Earl = str(data[x]['display_url'])
	target.write(Earl)
	target.write("\r")
	TimeStamp = str(data[x]['taken_at_timestamp'])
	target.write("\r")
	Height = str(data[x]['dimensions']['height'])
	target.write(Height)
	target.write("\r")	
	Width = str(data[x]['dimensions']['width'])
	target.write(Width)
	target.write("\r")	
	Caption = str(data[x]['edge_media_to_caption']["edges"][0]["node"])
	#['node'][u'text']
	target.write(Caption)
	target.write("\r")
	target.write("-----------------------------------------------------------------------------------------------")
	target.write("\r")
	x = x + 1
	
	
target.close()

#pprint(data)
#For printing the taxonomy
