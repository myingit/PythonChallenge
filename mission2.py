#!/usr/bin/python

import urllib2, time, re, collections

candidate_proxies = ['http://87.254.212.120:8080',
                     'http://10.158.100.3:8080',
                     'http://10.144.8.20:8080']
for proxy in candidate_proxies:
    print "Trying HTTP proxy %s..." % proxy
    proxy_handler = urllib2.ProxyHandler({'http':proxy})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    try:
        result = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read()
        print "Got URL using proxy %s" % proxy
        break
    except:
        print "Trying next HTTP proxy %s in 5 seconds" % proxy
        time.sleep(5)

text = re.findall(r'-->\n\n<!--\n([\s\S]*)\n-->',result)
reorder_text = ''.join([line.rstrip() for line in text[0]])
sum = collections.OrderedDict()
for char in reorder_text:
    sum[char] = sum.get(char,0) + 1
avgOC = len(text[0]) // len(sum)
next_page = ''.join([char for char in sum.keys() if sum[char] < avgOC]) + ".html"
print("The 3rd mission page is http://www.pythonchallenge.com/pc/def/" + next_page)