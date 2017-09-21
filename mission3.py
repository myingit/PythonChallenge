#!/usr/bin/python

import urllib2, time, re

candidate_proxies = ['http://87.254.212.120:8080',
                     'http://10.158.100.3:8080',
                     'http://10.144.8.20:8080']

for proxy in candidate_proxies:
    print "Trying HTTP proxy %s..." % proxy
    proxy_handler = urllib2.ProxyHandler({'http':proxy})
    opener = urllib2.build_opener(proxy_handler)
    urllib2.install_opener(opener)
    try:
        html_data = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read()
        print "Got URL using proxy %s" % proxy
        break
    except:
        print "Trying next HTTP proxy %s in 5 seconds" % proxy
        time.sleep(5)

target_data = re.findall(r'<!--([\s\S]*)-->',html_data)
arrange_data = target_data[0].replace("\n","")
final_data = "".join(re.findall(r'(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)',arrange_data)) + ".html"
print("The 4th mission page is http://www.pythonchallenge.com/pc/def/" + final_data)