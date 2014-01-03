#!/usr/bin/env python

import pprint
import sys
from os import environ as env

from swiftclient.client import get_auth, get_object
from swiftclient.exceptions import ClientException

auth_url = env.get('OS_AUTH_URL')
account = env.get('OS_TENANT_NAME')
user = env.get('OS_USERNAME')
key = env.get('OS_PASSWORD')

container = 'container1'
obj = 'data1MB.dat'
output_file = sys.argv[1]

try:
    pp = pprint.PrettyPrinter(indent=2)

    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url, acuser, key, auth_version='2.0')

    (resp_headers, obj_gen) = get_object(storage_url, token, container, obj,
                                         resp_chunk_size=65535)
    print "get_object response headers:"
    pp.pprint(resp_headers)
    print ""
    total_bytes = 0
    with open(output_file, 'wb') as fo:
        for chunk in obj_gen:
            chunk_len = len(chunk)
            total_bytes += chunk_len
            print "read %d byts" % chunk_len
            fo.write(chunk)

    print "Saved %d bytes to %s" % (total_bytes, output_file)
except ClientException, e:
    print e
except IOError, e:
    print e
