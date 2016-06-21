#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
USER_ID='PJR28TQ'
CONTACT_METHOD_ID='PSD17NZ'


def get_user_contact_method_by_id():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/users/{1}/contact_methods/{2}'.format(SUBDOMAIN, USER_ID, CONTACT_METHOD_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

