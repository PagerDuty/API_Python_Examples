#!/usr/bin/env python
import requests
import datetime
import json


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
SERVICE_IDS=['XYZ0ABC']

def create_maintenance_window(minutes=5):
"""Create a maintenance window starting now"""
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        "maintenance_window": {
            'start_time': datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ"),
            'end_time': (datetime.datetime.utcnow() + datetime.timedelta(minutes=minutes)).strftime("%Y-%m-%d %H:%M:%SZ"),
            "description": "Description goes here",
            "service_ids": PD_SERVICE_IDS,
        }
    }
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/maintenance_windows'.format(SUBDOMAIN),
                    headers=headers,
                    data=json.dumps(payload)
    )
    print r.status_code
    print r.text

