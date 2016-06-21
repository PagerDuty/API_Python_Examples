#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='zma9XjUU8tAjuzqnts1k'
USER_ID='PJR28TQ'


def create_user():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({"role":"admin",
                          "name":"Bart Sampsoniteus",
                          "email":"jfjfjfjfjfbart@eklejlejlk.com",
                          "requester_id":"{0}".format(USER_ID),})
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/users'.format(SUBDOMAIN),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

