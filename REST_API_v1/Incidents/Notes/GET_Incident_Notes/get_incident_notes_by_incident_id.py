#!/usr/bin/env python
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
INCIDENT_ID='PNJ1R1Y'

def get_notes_by_incident_id():
    url = 'https://{0}.pagerduty.com/api/v1/incidents/{1}/notes'.format(SUBDOMAIN, INCIDENT_ID)
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-Type': 'application/json',
    }
    r = requests.get(url, headers=headers)
    print r.status_code
    print r.json()

