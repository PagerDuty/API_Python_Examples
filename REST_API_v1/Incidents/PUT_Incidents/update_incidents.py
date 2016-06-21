#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
REQUESTER_ID='PJR28TQ'
INCIDENT_ID='PBI9MB9'

def update_incidents():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    params = {
        "requester_id": "{0}".format(REQUESTER_ID),
        "incidents": [
                        {
                            "id": "{0}".format(INCIDENT_ID),
                            "status": "resolved",
                        }
        ]
    }
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/incidents'.format(SUBDOMAIN),
                    headers=headers,
                    data=json.dumps(params)
    )
    print r.status_code
    print r.text
update_incidents()
