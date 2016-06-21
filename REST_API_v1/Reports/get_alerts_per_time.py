#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def get_alerts_per_time():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        'since':'2014-06-01',
        'until':'2014-06-12',
    }
    r = requests.get(
                    'https://{0}.pagerduty.com/api/v1/reports/alerts_per_time'.format(SUBDOMAIN),
                    headers=headers,
                    params=payload,
    )
    print r.status_code
    print r.text

