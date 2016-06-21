#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
USER_ID='PJR28TQ'

def get_users_log_entries():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/users/{1}/log_entries'.format(SUBDOMAIN, USER_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

