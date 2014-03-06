#!/usr/bin/env python

import pprint
import sys
from os import environ as env

from swiftclient.client import get_auth, put_object, put_container
from swiftclient.exceptions import ClientException

auth_url = env.get('OS_AUTH_URL')
account = env.get('OS_TENANT_NAME')
user = env.get('OS_USERNAME')
key = env.get('OS_PASSWORD')

container = 'test_put_object'
input_file = sys.argv[1]
obj = input_file


class read_wrapper(object):
    def __init__(self, fin):
        self.fin = fin

    def read(self, size=None):
        if size:
            print "try to read %d" % size
        return self.fin.read(size)

    def __getattr_(self, name):
        return getattr(self.fin, name)


try:
    pp = pprint.PrettyPrinter(indent=2)

    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url, acuser, key, auth_version='2.0')

    put_container(storage_url, token, container)

    resp_dict = {}
    with open(input_file, 'rb') as fin:
        fin2 = read_wrapper(fin)
        resp_etag = put_object(storage_url, token, container, obj,
                               contents=fin2, chunk_size=65535,
                               content_type="application/octet-stream",
                               response_dict=resp_dict)

    print "put_object return value:%s" % resp_etag
    print "put_object response headers:"
    pp.pprint(resp_dict)


except ClientException, e:
    print e
except IOError, e:
    print e
