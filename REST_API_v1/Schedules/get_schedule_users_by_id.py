#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SCHEDULE_ID='P6QNT52'

def get_schedule_by_id():
    url = 'https://{0}.pagerduty.com/api/v1/schedules/{1}/users'.format(SUBDOMAIN, SCHEDULE_ID)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    params = {
        'since':'2014-06-01',
        'until':'2014-06-12',
    }
    r = requests.get(url, headers=headers, params=params)
    print r.status_code
    print r.json()

