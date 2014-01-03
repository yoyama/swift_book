#!/usr/bin/env python

from swiftclient.client import get_auth, get_account, get_container
from swiftclient.exceptions import ClientException

auth_url = 'http://10.111.1.123:5000/v2.0'
account = 'test'
user = 'tester'
key = 'testing'


def subdir_proc(storage_url, token, container, subdir=None, nest=0):
    #print "DEBUG %s" % subdir
    (c_headers, objects) = get_container(storage_url, token,
                                         container,
                                         prefix=subdir,
                                         delimiter='/')
    spacer = ' ' * ((nest + 1) * 2)
    for obj in objects:
        if 'subdir' in obj:
            sdir_name = obj['subdir']
            l = len(sdir_name)
            idx = sdir_name.rfind('/', 0, l - 1)
            if idx >= 0:
                sdir_name = sdir_name[idx + 1:]
            print "%-30s" % (spacer + sdir_name)
            if subdir is None:
                new_subdir = obj['subdir']
            else:
                new_subdir = obj['subdir']
            subdir_proc(storage_url, token, container, new_subdir, nest + 1)
        else:
            if subdir is None:
                l = 0
            else:
                l = len(subdir)
            objname = obj['name'][l:]
            print "%-30s  %20s bytes" % (spacer + objname, obj['bytes'])

try:
    acuser = "%s:%s" % (account, user)
    (storage_url, token) = get_auth(auth_url, acuser, key, auth_version='2.0')

    (a_headers, containers) = get_account(storage_url, token)
    for container in containers:
        print "* %-30s%d objects % dbytes" % (container['name'],
                                              container['count'],
                                              container['bytes'])
        subdir_proc(storage_url, token, container['name'])
        print ""
except ClientException, e:
    print e
