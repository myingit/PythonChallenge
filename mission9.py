#!/usr/bin/env python
# coding:utf-8

"""
mission 9 steps:
1. hint from.page title 'connect the dots'
2. use 'base64.b64encode' to encode authentication information; use 'add_header' to add it to 'urllib2.Request' header.
   # request = urllib2.Request(url)
   # base64string = base64.b64encode('%s:%s' % (username, password))
   # request.add_header("Authorization", "Basic %s" % base64string)
   # html_data = urllib2.urlopen(request).read()
3. use 're.findall' twice to get the 'first' and 'second' string list from page source.
4. use map to change string list to numeric values.
5. use 'Image.new' to create new image; use 'ImageDraw.Draw' to draw the image.
6. use draw.polygon(xy,fill,outline) to connect the dots of 'first' and 'second'.
   xy – sequence of either 2-tuples like [(x, y), (x, y), ...] or numeric values like [x, y, x, y, ...]
   fill – color to use for the fill.
   outline – color to use for the outline.

if website use a login script for authentication. POST request method is needed to send encoded login data to website.
in this situation, 'urllib.urlencode' is needed to co-work with 'urllib2.Request' to submit login data in POST request.
usually the password should be encrypted. here is an example of md5 encrypted password.
   # username = "username_string"
   # password = hashlib.md5("password_string").hexdigest()
   # data = urllib.urlencode({'username':username,'password':password})
   # request = urllib2.Request(url,data)
   # html_data = urllib2.urlopen(request).read()
"""

import urllib2, time, base64, re
from PIL import Image, ImageDraw

url = "http://www.pythonchallenge.com/pc/return/good.html"
username = "huge"
password = "file"
candidate_proxies = [{},
                     {'http':'http://87.254.212.120:8080'},
                     {'http':'http://10.158.100.3:8080'},
                     {'http':'http://10.144.8.20:8080'}]

for proxy in candidate_proxies:
    print "Trying proxy %s..." % proxy.values()
    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    request = urllib2.Request(url)
    base64string = base64.b64encode('%s:%s' % (username, password))
    request.add_header("Authorization", "Basic %s" % base64string)
    try:
        html_data = urllib2.urlopen(request).read()
        print "Got URL using proxy %s" % proxy.values()
        break
    except:
        print "Trying next proxy in 5 seconds"
        time.sleep(5)

tmp_data = re.findall(r':\n([\d,\n]+)',html_data)
print(tmp_data)
first = map(int,re.findall(r'(\d+)',tmp_data[0]))
second = map(int,re.findall(r'(\d+)',tmp_data[1]))
print(first)
print(second)

img = Image.new('RGB',(500,500))
draw = ImageDraw.Draw(img)
draw.polygon(first,fill='white')
draw.polygon(second,fill='white')
img.show()