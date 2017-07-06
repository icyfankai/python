#!/usr/bin/python

import urllib2, json
from geturl import geturl
from key import value
import openpyxl, string, time
def getcontent(zone):
    secret_access_key = value.get('secret_access_key')
    access_key_id = value.get('access_key_id')
    data = { 
         'action':'DescribeBots',
         'version':'1',
         'signature_method':'HmacSHA256',
         'signature_version':'1',
    }
    url = geturl(data, zone, access_key_id, secret_access_key)
    header = {
        'user-agent': ('Mozilla/5.0 (Windows NT 6.2; WOW64)'
                       'AppleWebKit/537.36 (KHTML, like Gecko)'
                       'Chrome/56.0.2924.87 Safari/537.36'),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    }
    req = urllib2.Request(url, headers = header)
    response = urllib2.urlopen(req)
    page = response.read()
    content = json.loads(page)
    return content
