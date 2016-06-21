#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def get_incidents():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        'fields':'incident_number,status',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/incidents'.format(SUBDOMAIN),
                    headers=headers,
                    params=payload,
    )
    print r.status_code
    print r.text

