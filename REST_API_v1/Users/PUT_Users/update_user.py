#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='zma9XjUU8tAjuzqnts1k'
USER_ID='PG9E0O0'
#USER_ID='PJR28TQ'


def update_user():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({"role":"admin",
                          "name":"Bart Sampsoiteu",
                          "email":"jfjfjfjfjfbart@eklejlejlk.co",
    })
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/users/{1}'.format(SUBDOMAIN, USER_ID),
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

