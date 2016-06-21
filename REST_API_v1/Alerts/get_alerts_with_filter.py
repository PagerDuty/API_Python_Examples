#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def get_alerts_and_filter(since_date, until_date, filter_type):
    url = 'https://{0}.pagerduty.com/api/v1/alerts'.format(SUBDOMAIN)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    prms, prms['since_date'], prms['until_date'], prms['filter[type]'] = {}, since_date, until_date, filter_type
    r = requests.get(url, params=prms, headers=headers)
    print r.status_code
    print r.json()
