
from urllib2 import Request, urlopen, URLError

request = Request('http://eu.wgnwn.wgns.iv/rp/api/accounts/3001001263/')

response = urlopen(request)
body = response.read()
print body['invites_count']