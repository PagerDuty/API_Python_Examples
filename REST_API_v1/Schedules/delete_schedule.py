#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SCHEDULE_ID='P8R0I83'

def delete_schedule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.delete(
                    'https://{0}.pagerduty.com/api/v1/schedules/{0}'.format(SUBDOMAIN, SCHEDULE_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text

