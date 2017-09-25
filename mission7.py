#!/usr/bin/env python
# coding: utf-8

"""
mission 7 steps:
1. hint from the picture: there is a grey belt in the middle width of the picture.
2. use 'BytesIO' to create a buffered I/O implementation by using the in-memory bytes buffer read from 'urllib2.urlopen'.
3. use 'Image.open' to create the object of image.
4. use 'obj.getpixel' to get the pixel of the middle row of the picture.
5. gery pixel should have same value of r, g, b. remove all pixel of other color from 'mid_row'.
6. 'mid_row_grey' has lots of duplicates because each grey block's width is larger than 1 pixel.
   after counting, each block is exactly 7 pixels wide.
7. assume the integer value of r, g, b in 'element' is a ascii code, use 'map' with 'chr' to translate 'element'.
8. another number list is found in 'result', use 're.findall' to get all numbers.
9. use 'map' with 'int' to translate 'list_in_result' to a list with str type number, then use 'map' with 'chr' again.
10. get the final result 'integrity'.
"""

import urllib2,time, re
from PIL import Image
from io import BytesIO

url = "http://www.pythonchallenge.com/pc/def/oxygen.png"
candidate_proxies = [{},
                     {'http':'http://87.254.212.120:8080'},
                     {'http':'http://10.158.100.3:8080'},
                     {'http':'http://10.144.8.20:8080'}]

for proxy in candidate_proxies:
    print "Trying proxy %s..." % proxy.values()
    proxy_handler = urllib2.ProxyHandler(proxy)
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    try:
        html_data = urllib2.urlopen(url).read()
        print "Got URL using proxy %s" % proxy.values()
        break
    except:
        print "Trying next proxy in 5 seconds"
        time.sleep(5)

img = Image.open(BytesIO(html_data))

# get the pixel of the middle width row.
mid_row = [img.getpixel((x,img.height/2)) for x in range(img.width)]

# gery pixel should have same value of r, g, b. remove all pixel of other color from 'mid_row'
mid_row_grey = [r for r,g,b, a in mid_row if r == g == b]

# 'mid_row_grey' has lots of duplicates because each grey block's width is larger than 1 pixel.
# after counting, each block is exactly 7 pixels wide.
element = mid_row_grey[::7]

# assume the integer value of r, g, b in 'element' is a ascii code, use 'map' with 'chr' to translate 'element'.
result = "".join(map(chr,element))
print(result)

# another number list is found in 'result', use 're.findall' to get all numbers.
list_in_result = re.findall(r'(\d+)',result)

# use 'map' with 'int' to translate 'list_in_result' to a list with str type number, then use 'map' with 'chr' again.
final_result = "".join(map(chr,map(int,list_in_result)))
print(final_result)
print("We get it! The page of mission 8 is http://www.pythonchallenge.com/pc/def/"+ final_result + ".html")