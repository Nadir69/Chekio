__author__ = 'v_shabalin'
import requests

request = requests.get('http://eu.wgnwn.wgns.iv/rp/api/accounts/3001001263/')
print 'request:', request

response = requests.get('http://eu.wgnwn.wgns.iv/rp/api/accounts/3001001263/')
print 'response status code:', response.status_code
print 'response headers:', response.headers