#!/usr/bin/env python
import json
import requests


SUBDOMAIN = "" # Enter your subdomain here
API_ACCESS_KEY = "" # Enter your subdomain's API access key here


def ack_incident():
    """Acknowledges a triggered incident using the customer's API access key and incident key."""
    
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json'
    }

    payload = json.dumps({
        "service_key": "", # Enter the service key here
        "incident_key": "", # Enter the incident key here
        "event_type": "acknowledge",
        "description": "Andrew now working on the problem.", # Enter your own description
        "details": {
            "work started": "2010-06-10 05:43"
        }
    })

    r = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                      headers=headers,
                      data=payload,
    )

    print r.status_code
    print r.text


if __name__ == '__main__':
    ack_incident()
