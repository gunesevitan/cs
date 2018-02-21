# Chapter 13 Quiz


# 1.
# Who is credited with getting the JSON movement started?


# Douglas Crockford


# 2.
# What Python library do you have to import to parse and handle JSON?


# import json


# 3.
# What is the method used to parse a string containing JSON data
# so that you can work with the data in Python?


# json.loads()


# 4.
# What kind of variable will you get in Python when the following JSON is parsed:

# { "id" : "001",
#   "x" : "2",
#   "name" : "Chuck"
# }


# A dictionary with three key / value pairs


# 5.
# Which of the following is not true about the service-oriented approach?


# An application runs together all in one place


# 6.
# Which of these two web service approaches is preferred in
# most modern service-oriented applications?


# REST - Representational state transfer


# 7.
# What library call do you make to append properly encoded parameters
# to the end of a URL like the following:

# http://maps.googleapis.com/maps/api/geocode/json?sensor=false&address=Ann+Arbor%2C+MI


# urllib.parse.urlencode()


# 8.
# What happens when you exceed the Google geocoding API rate limit?


# You cannot use the API for 24 hours


# 9.
# What protocol does Twitter use to protect its API?


# OAuth


# 10.
# Which of the following is a web services approach used by the Twitter API?


# REST


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 13 Assignments


# Extracting Data from JSON


import json
import urllib.request

def parse_json(url):

    counts = []

    html = urllib.request.urlopen(url).read()
    json_dict = json.loads(html)

    for i in range(0, len(json_dict['comments'])):
        counts.append(int(json_dict['comments'][i]['count']))

    return sum(counts)

print(parse_json("http://python-data.dr-chuck.net/comments_42.json"))


# Using the GeoJSON API


import urllib.parse, urllib.request
import json

service_url = 'http://python-data.dr-chuck.net/geojson?'

while True:
    address = input("Enter location: ")

    if len(address) < 1 : break

    url = service_url + urllib.parse.urlencode({'sensor': 'false', 'address': address})

    uh = urllib.request.urlopen(url)
    data = uh.read()

    try:
        js = json.loads(str(data))
    except:
        js = None

    print(js["results"][0]["place_id"])
