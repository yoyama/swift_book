#!/usr/bin/env python

from swiftclient.client import get_auth
from swiftclient.exceptions import ClientException

auth_url = 'http://10.111.1.123:5000/v2.0'
account = 'test'
user = 'tester'
key = 'testing'

try:
    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url,
                                    acuser, key,
                                    auth_version='2.0')

    print "Storage URL: %s" % storage_url
    print "Token      : %s" % token

except ClientException, e:
    print e
