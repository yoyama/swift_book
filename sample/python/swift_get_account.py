#!/usr/bin/env python

import pprint

from swiftclient.client import get_auth, get_account, http_connection
from swiftclient.exceptions import ClientException

auth_url = 'http://10.111.1.123:5000/v2.0'
account = 'test'
user = 'tester'
key = 'testing'

try:
    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url, acuser, key, auth_version='2.0')
    conn = http_connection(storage_url)

    (headers, containers) = get_account(storage_url, token, http_conn=conn)
    pp = pprint.PrettyPrinter(indent=2)
    print "[Response headers]"
    pp.pprint(headers)

    print "[List of container]"
    pp.pprint(containers)

except ClientException, e:
    print e
