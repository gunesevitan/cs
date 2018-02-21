# Chapter 13 Quiz


# 1.
# What is "serialization" when we are talking about web services?


# The act of taking data stored in a program and formatting it so it can be sent across the network


# 2.
# Which of the following are not commonly used serialization formats?


# Dictionaries, HTTP, TCP


# 3.
# In this XML, which are the "simple elements"?

# <people>
#     <person>
#        <name>Chuck</name>
#        <phone>303 4456</phone>
#     </person>
#     <person>
#        <name>Noah</name>
#        <phone>622 7421</phone>
#     </person>
# </people>


# name, phone


# 4.
# In the following XML, which are attributes?

# <person>
#   <name>Chuck</name>
#   <phone type="intl">
#      +1 734 303 4456
#   </phone>
#   <email hide="yes" />
# </person>


# type, hide


# 5.
# In the following XML, which node is the parent node of node e

# <a>
#   <b>X</b>
#   <c>
#     <d>Y</d>
#     <e>Z</e>
#   </c>
# </a>


# c


# 6.
# Looking at the following XML, what text value would we find at path "/a/c/e"

# <a>
#   <b>X</b>
#   <c>
#     <d>Y</d>
#     <e>Z</e>
#   </c>
# </a>


# Z


# 7.
# What is the purpose of XML Schema?


# To establish a contract as to what is valid XML


# 8.
# If you were building an XML Schema and wanted to limit the values allowed in an xs:string field
# to only those in a particular list, what XML tag would you use in your XML Schema definition?


# xs:enumeration


# 9.
# What is a good time zone to use when computers are exchanging data over APIs?


# Universal Time / GMT


# 10.
# Which of the following is a web services approach used by the Twitter API?


# REST


# ----------------------------------------------------------------------------------------------------------------------


# Chapter 13 Assignments


# Extracting Data from XML


import urllib.request

from xml.etree import ElementTree as ET

def parse_xml(url):
    counts = []

    html = urllib.request.urlopen(url)
    tree = ET.parse(html)

    comments = tree.findall('comments/comment')

    for comment in comments:
        counts.append(int(comment.find('count').text))

    return sum(counts)

print(parse_xml("http://python-data.dr-chuck.net/comments_42.xml"))
