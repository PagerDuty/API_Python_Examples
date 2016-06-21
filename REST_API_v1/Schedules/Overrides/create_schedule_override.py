#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SCHEDULE_ID='P6QNT52'

def create_schedule_override():
    url = 'https://{0}.pagerduty.com/api/v1/schedules/{1}/overrides'.format(SUBDOMAIN, SCHEDULE_ID)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    payload = {
        "override": {
            "user_id": "PJR28TQ",
            "start": "2014-07-20",
            "end": "2014-07-22",
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(payload))
    print r.status_code
    print r.json()

