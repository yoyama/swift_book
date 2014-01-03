#!/usr/bin/env python

import pprint

from swiftclient.client import get_auth, http_connection
from swiftclient.client import get_account, head_account, post_account
from swiftclient.exceptions import ClientException

auth_url = 'http://10.111.1.123:5000/v2.0'
account = 'test'
user = 'tester'
key = 'testing'

try:
    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url, acuser, key, auth_version='2.0')
    conn = http_connection(storage_url)
    req_headers = {'X-Account-Meta-Test1': 'aaabbbccc',
                   'X-Account-Meta-Test2': '0123456789'}
    resp_headers = {}

    post_account(storage_url, token, req_headers,
                 response_dict=resp_headers, http_conn=conn)

    print "[Response headers of post_account()]"
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(resp_headers)
    print ""

    headers = head_account(storage_url, token, http_conn=conn)
    print "[Response headers of head_account()]"
    pp.pprint(headers)

except ClientException, e:
    print e
