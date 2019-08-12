#!/usr/bin/python

##
## August 11, 2019 00:36
##
## Written by John W Westerman
##        https://westerman.photo/
##
## Version 1.0.0

import requests
import json
import cssselect
from lxml import html

debug = 0 # set to 1 if you want to see more printed data

# The following are the fields I want to parse in the HTML data from the Ambient system.
InterestingFields = [ "CurrTime", "inBattSta", "outBattSta1", "inTemp", "inHumi", "AbsPress", "RelPress", "outTemp", "outHumi", "windir", "avgwind", "gustspeed", "dailygust", "solarrad", "uv", "uvi", "rainofhourly", "eventrain", "rainofdaily", "rainofweekly", "rainofmonthly", "rainofyearly" ]
url = "http://aw.ham.co/livedata.htm" # change to your URL
page = requests.get(url) # get the live data from the Ambient system
source = page.content # this is the result of the lookup
htmlElem = html.document_fromstring(source) # break it down into HTML elements
all_td_lines = htmlElem.cssselect("input") # get all the "<input>" elements from the html

Fields = {} # define and init the fields table
for tr in all_td_lines:
    if debug: print "evaluating for ", tr.name
    if tr.name in InterestingFields: # I'm only after the data interesting to me
        if debug: print tr.name, tr.value # print the value pairs
        Fields[tr.name] = tr.value # building a table of interesting field values to e converted to JSON later.

# This prints a JSON sentence of data. I put this in a SPLUNK database.
print "{ \"ambient1.ham.co\" : ", json.dumps(Fields),  "}"