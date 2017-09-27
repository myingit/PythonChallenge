#!/usr/bin/env python
# coding: utf-8

"""
mission 8 steps:
there is a bee in the picture. it sounds like busy too. What could that mean? bee? busy. busy? busy too ? bz2?
1. The hint in the password box says "inflate" so consider to use bz2 to decompress the strings.
2. use 're.findall' to get the 'un' and 'pw' strings from page source.
3. the 'un' and 'pw' strings gotten by 're.findall' use '\\' to indicate '\', this is because python saving encoding
   characters as string directly. in a string, symbol '\' should be escaped as '\\'. use 'decode("string_escape")' to
   remove escape.
4. use 'bz2.decompress' to get the username and password.
5. press the bee in the picture and input the username and password.
"""

import urllib2, time, re, bz2

url = "http://www.pythonchallenge.com/pc/def/integrity.html"
candidate_proxies = [
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

code = re.findall(r'[a-z]{2}: \'(.*)\'',html_data)
print(code)
un_compress = code[0].decode('string_escape')
pw_compress = code[1].decode('string_escape')
print([un_compress,pw_compress])
un = bz2.decompress(un_compress)
pw = bz2.decompress(pw_compress)
print("username is: " + un)
print("password is: " + pw)