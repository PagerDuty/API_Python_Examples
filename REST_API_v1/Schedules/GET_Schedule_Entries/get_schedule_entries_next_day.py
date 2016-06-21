#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SCHEDULE_ID='P6QNT52'

def get_schedule_entries():
    url = 'https://{0}.pagerduty.com/api/v1/schedules/{1}'.format(SUBDOMAIN, SCHEDULE_ID)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    payload = {
        "since": "2014-06-20",
        "until": "2014-06-22",
    }
    r = requests.get(url, headers=headers, params=payload)
    print r.status_code
    print r.json()

