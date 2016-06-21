#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
MAINTENANCE_WINDOW_ID='PEP41A8'
SERVICE_ID='PJGPSVN'

def update_maintenance_window():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = {
        "start_time":"2014-06-13T13:00:00-04:00Z",
        "end_time":"2014-06-16T14:00:00-04:00Z",
        "description":"Description goes here",
        "service_ids":["{0}".format(SERVICE_ID)],
    }
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/maintenance_windows/{1}'.format(SUBDOMAIN, MAINTENANCE_WINDOW_ID),
                    headers=headers,
                    data=json.dumps(payload),
    )
    print r.status_code
    print r.text

