#!/usr/bin/python

import urllib2, time, re

url_prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "12345"
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
        html_data = urllib2.urlopen(url_prefix + nothing).read()
        print "Got URL using proxy %s" % proxy.values()
        break
    except:
        print "Trying next proxy in 5 seconds"
        time.sleep(5)

page_num = re.findall(r'the next nothing is (\d+)',html_data)
while page_num:
    nothing = page_num[0]
    html_data = urllib2.urlopen(url_prefix + nothing).read()
    page_num = re.findall(r'the next nothing is (\d+)', html_data)
    print(html_data)
# break until html_data is "Yes, Divide by two and keep going".

page_num = [str(int(nothing)/2)]
print("OK. Let's divide by two and the next nothing is " + page_num[0])
while page_num:
    nothing = page_num[0]
    html_data = urllib2.urlopen(url_prefix + nothing).read()
    page_num = re.findall(r'the next nothing is (\d+)', html_data)
    print(html_data)
# break until find the final data "peak.html"

print("We get it! The 5th mission page is http://www.pythonchallenge.com/pc/def/" + html_data)