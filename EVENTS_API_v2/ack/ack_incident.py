#!/usr/bin/env python

import json
import requests

ROUTING_KEY = "" # ENTER EVENTS V2 API INTEGRATION KEY HERE 
INCIDENT_KEY = "" # ENTER INCIDENT KEY HERE 

def trigger_incident():
    # Triggers a PagerDuty incident without a previously generated incident key
    # Uses Events V2 API - documentation: https://v2.developer.pagerduty.com/docs/send-an-event-events-api-v2

    header = {
        "Content-Type": "application/json"
    }

    payload = { # Payload is built with the least amount of fields required to trigger an incident
        "routing_key": ROUTING_KEY, 
        "event_action": "acknowledge",
        "dedup_key": INCIDENT_KEY
    }

    response = requests.post('https://events.pagerduty.com/v2/enqueue', 
                            data=json.dumps(payload),
                            headers=header)
	
    if response.json()["status"] == "success":
        print ('Incident Acknowledged ')
    else:
        print response.text # print error message if not successful

if __name__ == '__main__':
    trigger_incident()