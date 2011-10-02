#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : tfluxadd.py
#
#* Purpose :
#
#* Creation Date : 02-10-2011
#
#* Last Modified : Sun 02 Oct 2011 02:45:15 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import urllib, urllib2, cookielib
import MultipartPostHandler
import sys
import conf

def parseIn():
  if len(sys.argv)==1:
    print "Usage: tfluxsend.py file(s)"
    return []
  else:
    forms=[]
    for f in sys.argv[1:]:
      forms.append({"url":open(f),"aid":"2"} )
    return forms

def main():
  forms = parseIn()
  if not forms:
    return 1
  else:
    username = conf.username
    password = conf.password
    address = conf.address
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'username' : username, 'iamhim' : password})
    opener.open('http://'+address+'/login.php', login_data)
    #print resp.readlines()
    for myform in forms:
      opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj),MultipartPostHandler.MultipartPostHandler)
      opener.open('http://'+address+'/dispatcher.php?action=fileUpload',myform)
      myform["url"].close()
    return 0


if __name__=="__main__":
  main()
