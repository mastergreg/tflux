#!/usr/bin/python
#/* -.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
#
#* File Name : tfluxadd.py
#
#* Purpose :
#
#* Creation Date : 02-10-2011
#
#* Last Modified : Sun 02 Oct 2011 03:07:17 PM EEST
#
#* Created By : Greg Liras <gregliras@gmail.com>
#
#_._._._._._._._._._._._._._._._._._._._._.*/

import urllib, urllib2, cookielib
import sys
import conf

def usage():
  print "Usage:tfluxadd.py torrentURL"

def main():
  if not len(sys.argv)==2:
    usage()
  else:
    username = conf.username
    password = conf.password
    address = conf.address
    T_FILE_LINK = sys.argv[1]
    myform = {"url": T_FILE_LINK,"aid":"2"}
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    login_data = urllib.urlencode({'username' : username, 'iamhim' : password})
    opener.open('http://'+address+'/login.php', login_data)
  #print resp.readlines()
    myform_data = urllib.urlencode(myform)
    opener.open('http://'+address+'/dispatcher.php?action=urlUpload',myform_data)

if __name__=="__main__":
  main()
