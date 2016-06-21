#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
INCIDENT_ID='PAHI1MA'
REQUESTER_ID='PJR28TQ'

def create_incident_note():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    params = {
        "requester_id":"{0}".format(REQUESTER_ID),
        "note":{
            "content":"New Note",
        }
    }
    r = requests.post(
                    'https://{0}.pagerduty.com/api/v1/incidents/{1}/notes'.format(SUBDOMAIN, INCIDENT_ID),
                    headers=headers,
                    data=json.dumps(params)
    )
    print r.status_code
    print r.text

