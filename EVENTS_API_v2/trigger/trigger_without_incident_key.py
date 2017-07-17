#!/usr/bin/env python
import json
import requests


SUBDOMAIN = "" # Enter your subdomain here
API_ACCESS_KEY = "" # Enter your subdomain's API access key here


def trigger_incident():
    """Triggers a PagerDuty incident without a previously generated incident key."""

    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }

    payload = json.dumps({
        "service_key": "", # Enter service key here
        "event_type": "trigger",
        "description": "FAILURE for production/HTTP on machine srv01.acme.com",
        "client": "Sample Monitoring Service",
        "client_url": "https://monitoring.service.com",
        "details": {
            "ping time": "1500ms",
            "load avg": 0.75
        }
    })

    r = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                      headers=headers,
                      data=payload,
    )

    print r.status_code
    print r.text


if __name__ == '__main__':
    trigger_incident()