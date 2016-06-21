#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
USER_ID='PJR28TQ'
CONTACT_METHOD_ID='PSD17NZ'


def create_contact_method():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({"contact_method":{"type":"SMS","address":"5551112222","label":"Island Lair","country_code":"1"}})
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/users/{1}/contact_methods'.format(SUBDOMAIN, USER_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

