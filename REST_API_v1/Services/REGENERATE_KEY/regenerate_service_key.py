#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_ID='PZ80FQV'


def regenerate_service():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/services/{1}/regenerate_key'.format(SUBDOMAIN, SERVICE_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

