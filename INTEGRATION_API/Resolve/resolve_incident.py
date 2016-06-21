#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'


def trigger_incident():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
              "service_key": "e05fd2270e2c4c028f3ae2388bbc09eb",
              "incident_key": "18d16696da65420c9f8d5cfa38b17a27",
              "event_type": "resolve",
              "description": "Andrew fixed the problem.",
              "details": {
                "fixed at": "2010-06-10 06:00"
              }
    })
    r = requests.post(
                    'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text
trigger_incident()
