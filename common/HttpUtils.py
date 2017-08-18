# coding = utf-8


import urllib
import urllib2
import sys
TYPE = sys.getfilesystemencoding()
print TYPE


def url_get(url, headers={}):
    req = urllib2.Request(url)
    res = urllib2.urlopen(req, headers=headers)
    print res.read().decode('utf-8').encode(TYPE)


def url_post(url, headers={}, body={}):
    data = urllib.urlencode(body)
    req = urllib2.Request(url=url, headers=headers, data=data)
    res = urllib2.urlopen(req)
    print res.read().decode('utf-8').encode(TYPE)

if __name__ == "__main__":
    # urlGet("http://www.baidu.com")
    url_post("http://www.baidu.com")
