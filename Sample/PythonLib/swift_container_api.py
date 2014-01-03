#!/usr/bin/env python

import pprint

from swiftclient.client import get_auth, get_container, head_container
from swiftclient.client import post_container, put_container, delete_container
from swiftclient.exceptions import ClientException

auth_url = 'http://10.111.1.123:5000/v2.0'
account = 'test'
user = 'tester'
key = 'testing'


try:
    pp = pprint.PrettyPrinter(indent=2)

    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url, acuser, key, auth_version='2.0')

    resp_dict = {}
    container = "container_api_test"
    print "put_container() %s" % container
    put_container(storage_url, token, container, response_dict=resp_dict)
    pp.pprint(resp_dict)

    print ""
    print "post_container() %s" % container
    pp.pprint(resp_dict)
    req_headers = {'X-Account-Meta-TestC1': 'aaabbbccc',
                   'X-Account-Meta-TestC2': '0123456789'}
    post_container(storage_url, token, container, req_headers,
                   response_dict=resp_dict)
    pp.pprint(resp_dict)

    print "head_container() %s" % container
    resp_dict = head_container(storage_url, token, container)
    pp.pprint(resp_dict)

    print "delete_container() %s" % container
    delete_container(storage_url, token, container, response_dict=resp_dict)
    pp.pprint(resp_dict)

except ClientException, e:
    print e
