# coding = utf-8
__author__ = 'zhaoshuai3'


import urllib
import urllib2,sys
type = sys.getfilesystemencoding()
print type

def urlGet(url,headers={}):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req,headers=headers)
    print res.read().decode('utf-8').encode(type)

def urlPost(url,headers={},body={}):
    data = urllib.urlencode(body)
    req = urllib2.Request(url = url ,headers=headers,data=data)
    res = urllib2.urlopen(req)
    print res.read().decode('utf-8').encode(type)

if __name__ == "__main__":
    # urlGet("http://www.baidu.com")
    urlPost("http://www.baidu.com")
