__author__ = 'v_shabalin'
import json, requests
from urllib2 import Request, urlopen
from pprint import pprint

def get_dictionary_from_url(url):
    request = Request(url)
    response = urlopen(request)
    body = response.read()
    parsed_body = json.loads(body)
    return parsed_body

requested_dictionary = get_dictionary_from_url('http://eu.wgnwn.wgns.iv/rp/api/accounts/3001001290/xp_factor/')
print requested_dictionary
print requested_dictionary['xp_amount']
