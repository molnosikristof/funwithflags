#some argparse here

import urllib, urllib2
params = {'cmd': 'ls -la'}
params = urllib.urlencode(params)
res = urllib2.urlopen('http://localhost:5000/cmd/', params)
data = res.read()
res.close()
