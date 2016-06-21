#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
USER_ID='PYZPJZ9'

def delete_user_by_id():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.delete(
                    'https://{0}.pagerduty.com/api/v1/users/{1}'.format(SUBDOMAIN, USER_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

