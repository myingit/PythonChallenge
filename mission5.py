#!/usr/bin/python

import urllib2, time, pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
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

unpickling = pickle.loads(html_data)
for line in unpickling:
#    line_str = ""
#    for element in line:
#        line_str = line_str + element[0]*element[1]
#    print(line_str)
    print("".join(element * count for element, count in line))
print("We get the picture 'channel'! The 6th mission page is http://www.pythonchallenge.com/pc/def/channel.html")