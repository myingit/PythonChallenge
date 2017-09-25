#!usr/bin/env python
# coding: utf-8

'''
purpose of mission6:
1. hint from source of 'channel.html' page: change 'html' to 'zip' to download a zip file.
2. use 'with...as...' to write the channel.zip file read from url into disk.
3. use 'zipfile.ZipFile(zipfile).read(file_in_zip)' to read the hint of readme.txt: start from 90052.txt
4. use while loop to get the end: 'Collect the comments'
5. use 'zipfile.ZipFile(zipfile).getinfo(file_in_zip).comment' to collect zip file comment info
'''

import urllib2,time, zipfile, os, tempfile, re

url = "http://www.pythonchallenge.com/pc/def/channel.zip"
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

zip_file = os.path.join(tempfile.gettempdir(),"channel.zip")
with open(zip_file,"wb") as raw_data:
    raw_data.write(html_data)

#print(zipfile.ZipFile(zip_file).namelist())
print(zipfile.ZipFile(zip_file).read("readme.txt"))

txt_num = ["90052"]
comments = ""
while txt_num:
    txt_data = zipfile.ZipFile(zip_file).read(txt_num[0] + ".txt")
    comments += zipfile.ZipFile(zip_file).getinfo(txt_num[0] + ".txt").comment
    print(txt_data)
    txt_num = re.findall(r'ext nothing is (\d+)',txt_data)
print(comments)