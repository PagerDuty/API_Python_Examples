#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
REQUESTER_ID='PJR28TQ'
INCIDENT_ID='PBI9MB9'

def resolve_incident():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    r = requests.put(
                    'https://{0}.pagerduty.com/api/v1/incidents/{0}/resolve'.format(SUBDOMAIN, INCIDENT_ID),
                    headers=headers,
    )
    print r.status_code
    print r.text
resolve_incident()
