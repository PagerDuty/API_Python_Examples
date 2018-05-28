#!/usr/bin/env python

import json
import requests

SERVICE_KEY = "" # ENTER EVENTS V1 API INTEGRATION KEY HERE 

def trigger_incident():
    # Triggers a PagerDuty incident without a previously generated incident key
    # Uses Events V1 API - documentation: https://v2.developer.pagerduty.com/docs/trigger-events

    payload = { # Payload is built with the least amount of fields required to trigger an incident
        "service_key": SERVICE_KEY, 
        "event_type": "trigger",
        "description": "Example alert on host1.example.com"
    }

    response = requests.post('https://events.pagerduty.com/generic/2010-04-15/create_event.json', 
                            data=json.dumps(payload))
	
    if response.json()["status"] == "success":
        print ('Incident created with with incident / alert key of ' + '"' + response.json()['incident_key'] + '"') 
    else:
        print response.text # print error message if not successful

if __name__ == '__main__':
    trigger_incident()