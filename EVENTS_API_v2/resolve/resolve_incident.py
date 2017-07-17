#!/usr/bin/env python
import json
import requests


SUBDOMAIN = "" # Enter your subdomain here
API_ACCESS_KEY = "" # Enter your subdomain's API access key here


def resolve_incident():
    """Resolves a PagerDuty incident using customer's API access key and incident key."""
    
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    
    payload = json.dumps({
              "service_key": "", # Enter service key here
              "incident_key": "", # Enter incident key here
              "event_type": "resolve",
              "description": "Andrew fixed the problem.", # Enter personalized description
              "details": {
                "fixed at": "2010-06-10 06:00"
              }
    })
    
    r = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                      headers=headers,
                      data=payload,
    )

    print r.status_code
    print r.text


if __name__ == '__main__':
    resolve_incident()
