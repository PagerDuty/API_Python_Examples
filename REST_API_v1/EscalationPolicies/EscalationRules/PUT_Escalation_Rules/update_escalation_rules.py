#!/usr/bin/env python
import json
import requests


SUBDOMAIN='pdt-dank'
API_ACCESS_KEY='HjEs6A6KozribnKqm1tX'
ESCALATION_POLICY_ID='P2LK6XG'


def update_escalation_rule():
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    {
         "escalation_rules": [
            {
              "escalation_delay_in_minutes": 12,
              "targets": [
                {
                  "type": "schedule",
                  "id": "PWEVPB6"
                }
              ]
            },
            {
              "id": "PNTPYK0",
              "escalation_delay_in_minutes": 24
            }
          ]
        }
    params = {
        "escalation_delay_in_minutes":44,
        "targets":[
            {
                "type":"user",
                "id":"PJR28TQ"
            }
        ]
    }
    r = requests.put(
                        'https://{0}.pagerduty.com/api/v1/escalation_policies/{1}/escalation_rules'.format(SUBDOMAIN, ESCALATION_POLICY_ID),
                        headers=headers,
                        data=json.dumps(params)
        )
    print r.status_code
    print r.text

