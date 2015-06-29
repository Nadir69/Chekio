__author__ = 'v_shabalin'
from urllib2 import Request, urlopen, URLError

request = Request('http://eu.wgnwn.wgns.iv/rp/api/accounts/3001001263/')

try:
	response = urlopen(request)
	body = response.read()
	print body
except URLError, e:
    print 'No response:', e

print body['invites_count']